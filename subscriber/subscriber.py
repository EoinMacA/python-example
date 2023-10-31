import socket
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define content type identifiers
CONTENT_TYPE_VIDEO = 0
CONTENT_TYPE_TEXT = 1
CONTENT_TYPE_AUDIO = 2

# Define offsets and lengths for header fields
HEADER_LENGTH = 1
CONTENT_TYPE_OFFSET = 0

subscriberIP = "localhost"
subscriberPort = 50002  # Choose a port for the subscriber

# Create a socket for the subscriber
subscriberSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the subscriber socket to its IP and port
subscriberSocket.bind((subscriberIP, subscriberPort))

print("Subscriber up and running")

while True:
    # Receive a message from the broker
    message, brokerAddress = subscriberSocket.recvfrom(1024)

    # Parse the received message to extract the content type from the header
    header = message[:HEADER_LENGTH]  # Extract the header
    content_type = int.from_bytes(header, byteorder='big')  # Extract content type

    if content_type == CONTENT_TYPE_VIDEO:
        # Handle video content (e.g., save video frame to a file)
        video_frame = message[HEADER_LENGTH:]  # Extract the video frame
        # Implement logic to process video frames (e.g., save to a file)
        # After processing the video frame, save it as an image
        with open('received_video_frame.jpg', 'wb') as file:
            file.write(video_frame)
        # Open the image with an image viewer
        # Implement this part based on your container's GUI capabilities
        logging.info(f"Received video frame from {brokerAddress}")
    elif content_type == CONTENT_TYPE_TEXT:
        # Handle text content (e.g., display text message)
        text_message = message[HEADER_LENGTH:]  # Extract the text message
        print(f"Received text message: {text_message.decode()}")
        logging.info(f"Received text message from {brokerAddress}: {text_message.decode()}")
    elif content_type == CONTENT_TYPE_AUDIO:
        # Handle audio content (e.g., process audio data)
        audio_data = message[HEADER_LENGTH:]  # Extract audio data
        # Implement logic to process audio data
        logging.info(f"Received audio content from {brokerAddress}")
