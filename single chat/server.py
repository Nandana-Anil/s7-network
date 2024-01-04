import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',8888)

server_socket.bind(server_address)
server_socket.listen(5)
print("server listeningg..")

client_socket,client_address=server_socket.accept()
print(f"accepted connection from {client_address}")

while True:
    data=client_socket.recv(1024).decode()
    print(f"client: {data}")

    if(data=="bye"):
        break

    message=input("server: ")
    client_socket.send(message.encode())

client_socket.close()
server_socket.close()