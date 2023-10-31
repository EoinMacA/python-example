# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the subscriber's source code and any necessary files into the container
COPY . /app

# Install any required Python packages (adjust this based on your subscriber's dependencies)
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variables (if needed)
ENV SUBSCRIBER_CONFIG=config.yaml

# Run the subscriber when the container launches
CMD ["python", "subscriber.py"]
