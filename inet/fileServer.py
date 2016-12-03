import socket
import threading
import os

def RetrFile(name, sock):
    print("hej")
    filename = sock.recv(1024)
    filename.decode('utf-8')
    print(filename)
    if os.path.isfile(filename):
        print("HÄR SKA VI VA")
        msg = b'Exists'
        #sock.send(msg.encode('utf-8'))
        sock.send(b'Exists')
        menuChoice = sock.recv(1024)
        menuChoice.decode('utf-8')
        if menuChoice[:1] != '4':
            with open(filename, 'r') as f:
                ammount = f.read(1024)
                sock.send(ammount.encode('utf-8'))
    else:
        print("WTF")
        msg = 'Error'
        sock.send(msg.encode('utf-8'))
    sock.close()

def Main():

    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print('Server started...')

    while True:
        c, addr = s.accept()
        print('Client connected:   ' + str(addr))
        t = threading.Thread(target = RetrFile, args = ("retrThread", c))
        t.start()
    s.close()

if __name__ == '__main__':
    Main()
