import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    clientNr = input("Whats your accountumber?   ")
    if clientNr != 'q':
        s.send(clientNr.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        #data.decode('utf-8')
        print (data)
        if data == 'Exists':
            choice = input('Check amount (1)\nWithdraw cash (2)\nDeposit cash (3)\nExit (4)\n')
            if choice != '4':
                s.send(choice.encode('utf-8'))
                f = open(clientNr, 'r')
                amount = s.recv(1024).decode('utf-8')
                if choice == '1':
                    print ('Current dSquared spending money left:  ' + amount)
                elif choice == '2':
                    withdrawal = input('Enter amount to withdraw: ')
                    withdrawal = str(int(withdrawal)*(-1))
                    print (withdrawal+amount)
                    s.send(withdrawFunc(amount, withdrawal))
                elif choice == '3':
                    withdrawal = input('Enter amount to withdraw: ')
                    s.send(withdrawFunc(amount, withdrawal))
                else:
                    pass
                    #försök igen
            else:
                return ('sorry')
    s.close()


def withdrawFunc(a, w):
    a = str(int(a)+int(w))
    print (a)
    return a.encode('utf-8')



if __name__ == '__main__':
    Main()

