import socket


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('serving HTTP on port... ' + str(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print (request.decode('utf-8'))

    http_response = """\
    HTTP/1.1 200 OK

    Hello, World!
    """
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()




    import socket
import sys
from _thread import *

host, port = '', 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('Connecting to bank...')

def threaded_client(connection):
    connection.send(str.encode('Welcome to bank, what would you like to do \n Check balance (1) \n Withdrawal (2) \n Deposit(3) \n Exit(4)'))

    #infinite loop to keep connection running and up to date
    while True:
        #10 bytes
        data = connection.recv(10)
        reply = 'Your OPTION was finished, your current balance is:...'
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    connection, adress = s.accept()
    print('Connected to: ' +adress[0]+ ':' + str(adress[1]))

    start_new_thread(threaded_client, (connection,))