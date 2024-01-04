import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address=('localhost',8888)

while True:
    message=input("client message: ")
    client_socket.sendto(message.encode(),server_address)

    data,_=client_socket.recvfrom(1024)
    print(f"client recieved: {data.decode()}")