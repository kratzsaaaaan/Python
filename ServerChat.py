import socket
import threading
import base64

name = input('Your name: ')

def connection():
    print('...')
    host = input('Ip adress: ')
    port = int(input('Port: '))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Listening...')
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            
            t = threading.Thread(target=recvmsg, args=(conn,))
            t1 = threading.Thread(target=sendmsg, args=(conn,))
            
            t.start()
            t1.start()
            t.join()
            t1.join()

def recvmsg(conn):
     while True:
            data = conn.recv(1024)
            if data:
                print('           ',base64.b64decode(data).decode())
            else:
                pass
            
def sendmsg(conn):
    while True:
        msg = name + ': ' + input("")
        mssg = bytes(msg.encode('utf-8'))
        conn.sendall(encoder(mssg))
        
def encoder(msg):
    msgencod = base64.b64encode(msg)
    return bytes(msgencod)
        
connection()
