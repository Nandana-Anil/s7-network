import socket

server_address=('localhost',8888)

def caesar_encrypt(text,shift):
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
    client_socket=socket.socket()
    client_socket.connect(server_address)
    message=input("enter text to encrypt: ")
    shift=int(input("enter shift value: "))
    res=caesar_encrypt(message,shift)

    print(f"encrypted: {res}")
    client_socket.send(res.encode())

    client_socket.close()
main()
