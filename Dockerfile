# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for compiling Python packages
RUN apt-get update \
    && apt-get install -y gcc libc-dev

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your Flask app runs on
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=server.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
