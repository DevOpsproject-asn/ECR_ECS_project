# Use a base image with Python installed
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY server.py /app

# Expose the port the server runs on
EXPOSE 8000

# Command to run the HTTP server
CMD ["python", "-m", "http.server", "8000"]

