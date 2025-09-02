import socket

s = socket.socket()
s.bind(('localhost', 8000))   
s.listen(5)                  
print("Server is waiting for connection...")

c, addr = s.accept()
print("Connected with:", addr)

while True:
    i = input("Enter Data: ")
    if not i:  
        print("Closing connection...")
        c.close()
        break

    c.send(i.encode())       
    ack = c.recv(1024).decode() 

    if ack:
        print("Client:", ack)
    else:
        print("Client disconnected")
        c.close()
        break