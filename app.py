from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "student_feedback_devops_secret_key"

FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedback.txt")


def load_feedbacks():
    """Reads feedbacks from feedback.txt and returns a parsed list of dicts."""
    feedbacks = []
    if not os.path.exists(FEEDBACK_FILE):
        return feedbacks

    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if not content:
            return feedbacks

        entries = content.split("\n---\n")
        for entry in entries:
            clean_entry = entry.strip()
            if not clean_entry:
                continue

            item = {
                "name": "Anonymous",
                "department": "General",
                "email": "",
                "rating": "5",
                "feedback": "",
                "submitted": "",
            }

            for line in clean_entry.split("\n"):
                if ": " in line:
                    key, val = line.split(": ", 1)
                    norm_key = key.strip().lower()
                    if norm_key in item:
                        item[norm_key] = val.strip()

            if item["feedback"]:
                feedbacks.append(item)

        # Most recent first
        return list(reversed(feedbacks))
    except Exception as e:
        print(f"Error reading {FEEDBACK_FILE}: {e}")
        return feedbacks


def save_feedback(name, department, email, rating, feedback_text):
    """Appends a single feedback entry to feedback.txt."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    # Clean up multi-line text to single lines or normalized spaces
    clean_feedback = " ".join(feedback_text.strip().splitlines())

    entry = (
        f"Name: {name.strip()}\n"
        f"Department: {department.strip()}\n"
        f"Email: {email.strip()}\n"
        f"Rating: {rating.strip()}\n"
        f"Feedback: {clean_feedback}\n"
        f"Submitted: {timestamp}\n"
        f"---\n"
    )

    with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


@app.route("/")
def index():
    """Homepage showcasing Hero, Features, DevOps Workflow, and About sections."""
    return render_template("index.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    """Form to submit student feedback."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        department = request.form.get("department", "").strip()
        email = request.form.get("email", "").strip()
        rating = request.form.get("rating", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        if not name or not department or not email or not rating or not message:
            flash("Please fill in all required fields.", "error")
            return render_template(
                "feedback.html",
                form_data={
                    "name": name,
                    "department": department,
                    "email": email,
                    "rating": rating,
                    "message": message,
                },
            )

        try:
            rating_num = int(rating)
            if rating_num < 1 or rating_num > 5:
                raise ValueError()
        except ValueError:
            flash("Rating must be between 1 and 5.", "error")
            return render_template(
                "feedback.html",
                form_data={
                    "name": name,
                    "department": department,
                    "email": email,
                    "rating": rating,
                    "message": message,
                },
            )

        # Save to file
        save_feedback(name, department, email, rating, message)
        flash("Feedback submitted successfully!", "success")
        return render_template("feedback.html", submitted=True)

    return render_template("feedback.html")


@app.route("/view-feedback")
def view_feedback():
    """Displays submitted feedbacks."""
    feedbacks = load_feedbacks()
    return render_template("view_feedback.html", feedbacks=feedbacks)


@app.route("/about")
def about():
    """Direct route to About section."""
    return redirect(url_for("index") + "#about")


@app.route("/devops")
def devops():
    """Direct route to DevOps workflow section."""
    return redirect(url_for("index") + "#devops")


if __name__ == "__main__":
    # Ensure feedback.txt exists
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
            pass

    # Run accessible on all interfaces for Docker container compatibility
    app.run(host="0.0.0.0", port=5000, debug=True)
