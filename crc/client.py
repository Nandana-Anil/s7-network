import socket

key="1101"
server_address=('localhost',8888)

def xor(a,b):
    result=[]
    for i in range(1,len(a)):
        if(a[i]==b[i]):
            result.append("0")
        else:
            result.append("1")
    return "".join(result)

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

def encrypt(data):
    len_key=len(key)
    appended=data+"0"*(len_key-1)
    rem=mod2div(appended)
    encrypted=data+rem
    return encrypted

def main():
    client_socket=socket.socket()
    client_socket.connect(server_address)

    message=input("enter data to send to server: ")
    data=encrypt(message)
    print(f"encrypted: {data}")
    client_socket.send(data.encode())
    client_socket.close()

main()