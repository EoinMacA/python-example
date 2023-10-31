# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the producer's source code and any necessary files into the container
COPY . /app

# Install any required Python packages (adjust this based on your producer's dependencies)
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose any necessary ports (adjust this based on your producer's configuration)
EXPOSE 8081

# Define environment variables (if needed)
ENV PRODUCER_PORT=8081
ENV PRODUCER_CONFIG=config.yaml

# Run the producer when the container launches
CMD ["python", "producer.py"]
