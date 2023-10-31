import socket

# Define content type identifiers
CONTENT_TYPE_VIDEO = 0
CONTENT_TYPE_TEXT = 1
CONTENT_TYPE_AUDIO = 2

# Define offsets and lengths for header fields
HEADER_LENGTH = 1
CONTENT_TYPE_OFFSET = 0

brokerIP = "localhost"
brokerPort = 50001  # Choose a port for the broker

# Create a socket for the broker
brokerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the broker socket to its IP and port
brokerSocket.bind((brokerIP, brokerPort))

print("Broker up and running")

# Define the server's address and port
serverAddressPort = ("localhost", 50000)

# Listen for incoming messages from clients
while True:
    # Receive a message from a client
    message, clientAddress = brokerSocket.recvfrom(1024)

    # Parse the received message to extract the content type from the header
    header = message[:HEADER_LENGTH]  # Extract the header
    content_type = int.from_bytes(header, byteorder='big')  # Extract content type

    if content_type == CONTENT_TYPE_VIDEO:
        # Handle video content (forward the video frame to the server)
        video_frame = message[HEADER_LENGTH:]  # Extract the video frame
        brokerSocket.sendto(video_frame, serverAddressPort)
    elif content_type == CONTENT_TYPE_TEXT:
        # Handle text content (forward the text message to the server)
        text_message = message[HEADER_LENGTH:]  # Extract the text message
        brokerSocket.sendto(text_message, serverAddressPort)
    elif content_type == CONTENT_TYPE_AUDIO:
        # Handle audio content (forward the audio data to the server)
        audio_data = message[HEADER_LENGTH:]  # Extract the audio data

        # Implement logic to process audio data (e.g., save to a file, process it, etc.)
        # For example, you could save the audio data to an audio file
        audio_filename = "received_audio.wav"  # Replace with the desired filename
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(audio_data)

    # Print the received message and client address
    if content_type == CONTENT_TYPE_TEXT:
        print(f"Received from {clientAddress}: {message[HEADER_LENGTH:].decode()}")
    else:
        print(f"Received from {clientAddress}: {message}")


    # Forward the message to the server
    brokerSocket.sendto(message, serverAddressPort)

    # Add handling for other content types as necessary
