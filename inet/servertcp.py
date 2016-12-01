import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    print('Waiting for customer...')
    s.listen(2)
    connection, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        print ("from connected user:" + data)
        data = data.upper()
        print('sending: ' + data)
        connection.send(data.encode('utf-8'))
    connection.close()

if __name__ == '__main__':
    Main()
