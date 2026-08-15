from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        register_number = request.form["register_number"]
        department = request.form["department"]
        rating = request.form["rating"]
        feedback_text = request.form["feedback"]

        # Store feedback in a text file
        with open("feedback.txt", "a") as file:
            file.write(
                f"Name: {name}, "
                f"Register Number: {register_number}, "
                f"Department: {department}, "
                f"Rating: {rating}, "
                f"Feedback: {feedback_text}\n"
            )

        return "<h2>Feedback submitted successfully!</h2><a href='/'>Submit another feedback</a>"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)