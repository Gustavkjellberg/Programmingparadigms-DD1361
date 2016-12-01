import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    clients =  []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    s.setblocking(0)

    print('Server started')

    quitting = False

    while not quitting:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            if '4' in data:
                quitting = True
            else:
                print(data)
                if '1' in data:
                    print("Withdraw")
                    msg = "Withdraw"

            if addr not in clients:
                clients.append(addr)
            print (str(addr) + data)

            s.sendto(msg.encode('utf-8'), addr)
            #s.sendto(data, addr)

        except:
            pass
    s.close()



    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Message from: ' + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending" + data)
        s.sendto(data.encode('utf-8'), addr)

    c.close()

if __name__ == '__main__':
    Main()
