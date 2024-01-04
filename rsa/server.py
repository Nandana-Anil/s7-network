import socket
import pickle


server_socket = socket.socket()
server_address = ("127.0.0.1",8888)
server_socket.bind(server_address)
server_socket.listen(5)

client_socket, client_address = server_socket.accept()

key = client_socket.recv(1024)
e,n = pickle.loads(key)
msg = client_socket.recv(1024).decode()
print(f"to be Encrypted Message: {msg}")
encrypted_msg = pow(int(msg),e,n)
print(encrypted_msg)

client_socket.send(str(encrypted_msg).encode())

client_socket.close()
server_socket.close()