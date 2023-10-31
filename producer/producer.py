import socket
from pydub import AudioSegment

# Define the IP and port of the broker
brokerIP = "localhost"
brokerPort = 50001  # Choose the broker's port

# Create a socket for the producer
producerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the header format with a content type field
HEADER_LENGTH = 1  # Define the length of the header
CONTENT_TYPE_OFFSET = 0  # Offset of the content type field in the header

# Define content type identifiers
CONTENT_TYPE_VIDEO = 0
CONTENT_TYPE_TEXT = 1
CONTENT_TYPE_AUDIO = 2

print("Producer up and running")

# Inside your loop
while True:
    # Depending on the content type, send different content
    content_type = CONTENT_TYPE_VIDEO  # Set the content type for video

    if content_type == CONTENT_TYPE_VIDEO:
        # Open and read the video frame image file (assuming it's named 'my_image.jpg')
        with open('my_image.jpg', 'rb') as file:
            video_frame = file.read()

        # Create a message with the header and video frame content
        header = content_type.to_bytes(HEADER_LENGTH, byteorder='big')
        message = header + video_frame
    elif content_type == CONTENT_TYPE_TEXT:
        # Open and read the text message from the text file (assuming it's named 'sample_text.txt')
        with open('sample_text.txt', 'r') as file:
            text_message = file.read()

        # Set the content type for text
        content_type = CONTENT_TYPE_TEXT

        # Create a message with the header and text message content
        header = content_type.to_bytes(HEADER_LENGTH, byteorder='big')
        message = header + text_message.encode('utf-8')
    elif content_type == CONTENT_TYPE_AUDIO:
        # Load and convert the audio from MP3 to WAV
        audio_mp3 = AudioSegment.from_mp3('sample_audio.mp3')
        audio_mp3.export('sample_audio.wav', format='wav')
        
        # Open the WAV file
        with open('sample_audio.wav', 'rb') as file:
            audio_data = file.read()

        # Set the content type for audio
        content_type = CONTENT_TYPE_AUDIO

        # Create a message with the header and audio data
        header = content_type.to_bytes(HEADER_LENGTH, byteorder='big')
        message = header + audio_data

    # Send the message to the broker
    producerSocket.sendto(message, (brokerIP, brokerPort))

    # Switch to the next content type in a cyclic manner
    content_type = (content_type + 1) % 3
