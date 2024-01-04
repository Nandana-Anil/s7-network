import socket
import pickle

server_address=('localhost',8888)

def lzw_decompress(data):
    dictionary={i:chr(i) for i in range(256)}
    result=[]

    w=dictionary[data.pop(0)]
    result.append(w)
    for k in data:
        if k in dictionary:
            entry=dictionary[k]
        elif k==len(dictionary):
            entry=w+w[0]
        else:
            raise ValueError("error in compression")
        result.append(entry)
        dictionary[len(dictionary)]=w+entry[0]
        w=entry
    return ''.join(result)


def main():
    server_socket=socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(2)
    print("server listening...")

    client_socket,client_address=server_socket.accept()
    print(f"accepted connection from {client_address}")

    data_temp=client_socket.recv(1024)
    data=pickle.loads(data_temp)
    print(f"recieved data: {data}")

    res=lzw_decompress(data)
    print(f"decompressed : {res}")

main()