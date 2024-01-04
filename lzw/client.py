import socket
import pickle

server_address=('localhost',8888)

def lzw_compress(data):
    dictionary={chr(i):i for i in range(256)}
    result=[]
    w=""
    for char in data:
        wc=w+char
        if wc in dictionary:
            w=wc
        else:
            result.append(dictionary[w])
            dictionary[wc]=len(dictionary)
            w=char
    if w:
        result.append(dictionary[w])

    print("dictionary: ")
    for k,v in dictionary.items():
        print(f"{k}:{v}")
    return result


def main():
    client_socket=socket.socket()
    client_socket.connect(server_address)

    message=input("enter data to send: ")
    res=lzw_compress(message)
    res_pickle=pickle.dumps(res)
    print(f"compressed: {res}")

    client_socket.send(res_pickle)
    client_socket.close()

main()
