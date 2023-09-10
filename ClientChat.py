import socket
import threading
import base64

name = input('Your name: ')

def connection():
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('Host: ')
    port = int(input('Port: '))
    sockets.connect((host, port))
    print("Connected in ", host)
    t = threading.Thread(target=recvmessage, args=(sockets,))
    t1 = threading.Thread(target=sendmessage, args=(sockets,))
    t1.start()
    t.start()
    t.join()
    t1.join()
    
def sendmessage(socket):
    while True:
        msg = input("")
        mssg = name + ': ' + msg
        msssg = bytes(mssg.encode('utf-8'))
        socket.sendall(encoder(msssg))
        if msg == 'quit':
            socket.close()
            exit()
    
def recvmessage(socket):
    while True:
        data = socket.recv(1024)
        print('            ',decoder(data))
        
def encoder(msg):
    msgencoded = base64.b64encode(msg)
    return bytes(msgencoded)

def decoder(msg):
    return base64.b64decode(msg).decode()

connection()