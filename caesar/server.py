import socket

server_address=('localhost',8888)

def caesar_decrypt(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            shifted=ord(char)+shift
            if char.islower():
                if (shifted<ord('a')):
                    shifted+=26
                elif(shifted>ord('z')):
                    shifted-=26
            elif char.isupper():
                if (shifted<ord('A')):
                    shifted+=26
                elif(shifted>ord('Z')):
                    shifted-=26
            result+=chr(shifted)
        else:
            result+=char
    return result

def main():
    server_socket=socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(4)
    print("server is listening...")

    client_socket,client_address=server_socket.accept()
    print(f"accepted connection from {client_address}")

    data=client_socket.recv(1024).decode()

    print(f"recieved: {data}")
    shift=int(input("enter shift value for decryption: "))

    dec=caesar_decrypt(data,-shift)
    print(f"decrypted: {dec}")

main()
