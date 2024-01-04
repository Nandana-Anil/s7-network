import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',8888)

server_socket.bind(server_address)

server_socket.listen(5)

print("server waiting for client")

while True:
    client_socket, client_address = server_socket.accept()

    print("accepted connection from ",client_address)

    data=client_socket.recv(1024)
    print(f"recieved message: {data.decode()}")

    message=input("enter message to send to client: ")
    client_socket.send(message.encode())

    client_socket.close()