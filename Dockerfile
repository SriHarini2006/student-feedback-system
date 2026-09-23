# Use official lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Set environment variables:
# Prevent Python from writing .pyc files to disc and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy dependency definition and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files into container
COPY . .

# Expose port 5000 for Flask web server
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
