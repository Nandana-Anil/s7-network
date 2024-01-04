import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=('localhost',8888)

server_socket.bind(server_address)

print("server listening...")

while True:
    data,client_address=server_socket.recvfrom(1024)

    print(f"data recieved: {data.decode()}")

    message=input("server message: ")
    server_socket.sendto(message.encode(),client_address)

