import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    clientNr = input("Whats your accountumber?   ")
    if clientNr != 'q':
        print("hejsahjsa")
        s.send(clientNr.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        #data.decode('utf-8')
        print (data)
        if data == 'Exists':
            print("HÄR?")
            choice = input('press 1 ')
            if choice == '1':
                s.send(choice.encode('utf-8'))
                f = open(clientNr, 'r')
                ammount = s.recv(1024).decode('utf-8')
                #ammount.decode('utf-8')
                print (ammount)
                #f.write(data)

            else:
                return ('sorry')
        print("HÄR=??!!!")
    s.close()


if __name__ == '__main__':
    Main()

