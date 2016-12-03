import socket
import sys
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
            #dat, add = s.recvfrom(1024)
            #dat = dat.decode('utf-8')
            print(data)

            #hej = "_*_*_*_*_*_*_*_*_*"
            #s.sendto(hej.encode('utf-8'), addr)
            #print (hej)
            msg = menu(data, addr,s)

            # if 'Enter' in msg:
            #   ropa på engMeny
            #   returnera
            if addr not in clients:
                clients.append(addr)
            print (str(addr) + data)

            #s.sendto(hej.encode('utf-8'), addr)
            #s.sendto(data, addr)

        except:
            pass
    s.close()


def menu(data, addr, s):
    print("HEJEHEJEJ")
    if '1' in data:
        #if msg not none:
        msg = 'Ange kontonummer\n\n'
        s.sendto(msg.encode('utf-8'), addr)
        sweMen(addr, s)
        return 'a'
        #svenska meny
    elif '2' in data:
        msg =  'Enter accountnumber\n\n'
        s.sendto(msg.encode('utf-8'), addr)
        engMen(data, addr)
        return 'a'
        #eng meny
    elif '3' in data:
        return True
    else:
        return 'Fel, gör om'


def sweMen(addr, s):
    print("SWEMEN")
    optionsSwe = 'Kontoutdrag (1)\nUttag (2)\nInsättning (3)\nBytspåk (4)\nAvsluta (5)\n\n'
    s.sendto(optionsSwe.encode('utf-8'), addr)
    #data, addr = s.recvfrom(1024)
    #data = data.decode('utf-8')
    #print (data)
    cash(data, addr, s)


def cash(data, addr, s):
    #read
    ammount = 1000
    if '1' in data:
        msg = str(ammount)
        s.sendto(msg.encode('utf-8'), addr)
    elif '2' in data:
        msg = 'Enter ammount to withdraw from your current ' + str(ammount)
        s.sendto(msg.encode('utf-8'), addr)
    else:
        pass





    pass



    """while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Message from: ' + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending" + data)
        s.sendto(data.encode('utf-8'), addr)

    c.close()"""

if __name__ == '__main__':
    Main()
