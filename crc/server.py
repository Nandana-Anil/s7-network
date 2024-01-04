import socket

key="1101"
server_address=('localhost',8888)

def xor(a,b):
    res=[]
    for i in range(1, len(a)):
        if(a[i]==b[i]):
            res.append("0")
        else:
            res.append("1")
    return "".join(res)

def mod2div(data):
    cipher_len=len(key)
    cipher=data[0:cipher_len]

    while(cipher_len<len(data)):
        if(cipher[0]=="1"):
            cipher=xor(cipher,key)+data[cipher_len]
        else:
            cipher=xor(cipher,"0"*cipher_len)+data[cipher_len]
        cipher_len+=1

    if(cipher[0]=="1"):
        cipher=xor(cipher,key)
    else:
        cipher=xor(cipher,"0"*cipher_len)
    return cipher

def decrypt(data):
    len_key=len(key)
    appended=data+"0"*(len_key-1)
    rem=mod2div(appended)
    return rem

def main():
    server_socket=socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(5)

    client_socket,client_addr=server_socket.accept()
    data=client_socket.recv(1024).decode()
    print(f"recieved data: {data}")
    rem=decrypt(data)
    print(f"remainder: {rem}")
    check="0"*(len(key)-1)
    if(check==rem):
        print("no error")
    else:
        print("error")

main()