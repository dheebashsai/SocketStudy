import socket

# Create socket
s = socket.socket()
s.connect(('localhost', 8000))   # Connect to server
print("Connected to server...")

while True:
    data = s.recv(1024).decode()   # Receive data
    if not data:   # If no data, server closed
        print("Server disconnected")
        break

    print("Server:", data)
    ack = "Got it: " + data
    s.send(ack.encode())   # Send acknowledgment