# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the broker's source code and any necessary files into the container
COPY broker.py /app/

# Install any required Python packages (adjust this based on your broker's dependencies)
# Skip pip installation


# Expose the port your broker listens on (adjust this to match your broker's configuration)
EXPOSE 8080

# Define environment variables (if needed)
ENV BROKER_PORT=8080
ENV BROKER_CONFIG=config.yaml

# Run the broker when the container launches
CMD ["python", "broker.py"]
