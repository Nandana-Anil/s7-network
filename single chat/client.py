import socket

server_address=('localhost',8888)

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    message=input("client: ")
    client_socket.send(message.encode())

    if(message=="bye"):
        break

    data=client_socket.recv(1024)
    print(f"server: {data.decode()}")

client_socket.close()