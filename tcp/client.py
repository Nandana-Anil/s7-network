import socket

server_address=('localhost',8888)

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)

message=input("enter message to send server: ")
client_socket.send(message.encode())

data=client_socket.recv(1024)
print(f"recieved from server: {data.decode()}")