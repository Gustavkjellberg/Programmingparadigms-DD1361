import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    language(s)



def language(s, clientNr = None, data = None):
    lg = input('Fortsätt på svenska (1)\nContinue in english (2)\n')

    if clientNr == None:

        if lg == '1':
            clientNr = input("Ange kontonummer?   ")
            clientCode = input("Ange kod: ")
        elif lg == '2':
            clientNr = input("What's your accountumber?   ")
            clientCode = input("Ange kod: ")
        else:
            print("We do not support any other language, please choose among the alternatives")
            language(s)
        s.send(clientNr.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        s.send(clientCode.encode('utf-8'))
        passOk = s.recv(1024).decode('utf-8')
        print (passOk)
        if passOk == 'noPass':
            language(s)
        else:
            pass
    else:
        pass

    if data == 'Exists':
        if lg == '1':
            sweMen(s, clientNr, data, lg)
        else:
            engMen(s, clientNr, data, lg)





#sends och recvs max 10 bytes


def sweMen(s, clientNr, data, lg):
    s.send(lg.encode('utf-8'))
    banner = s.recv(1024).decode('utf-8')
    print(banner)
    codeget = s.recv(10).decode('utf-8')
    codeList = codeget
    i = 0
    while i <= 14:
        i += 1
        if i < 15:
            codeget = s.recv(10).decode('utf-8')
            codeList += codeget
        else:
            pass
    choice = input('Saldo (1)\nTa ut pengar (2)\nSätt in pengar (3)\nChange language (4)\nAvsluta (5)\n')
    if choice != '5':
        s.send(choice.encode('utf-8'))
        #f = open(clientNr, 'r')
        amount = s.recv(1024).decode('utf-8')
        if choice == '1':
            print ('Saldo:  ' + amount)
            sweMen(s, clientNr, data, lg)
        elif choice == '2':
            code = input('Ange säkerhetskod: ')
            if code in codeList:
                withdrawal = input('Ange summa att ta ut: ')
                withdrawal = str(int(withdrawal)*(-1))
                s.send(withdrawFunc(amount, withdrawal))
                sweMen(s,clientNr, data, lg)
            else:
                print('Fel, vänligen gör om')
                sweMen(s, clientNr, data, lg)
        elif choice == '3':
            withdrawal = input('Hur  mycket ill du sätta in?: ')
            s.send(withdrawFunc(amount, withdrawal))
            sweMen(s, clientNr, data, lg)
        elif choice == '4':
            language(s, clientNr, data)
        else:
            pass
            print('Ogiltligt val, försök igen!')
            sweMen(s, clientNr, data, lg)
    else:
        return ('Tack för besöket!')
    s.close()


def codeRecv(s):
    codeget = s.recv(10).decode('utf-8')
    codeList = codeget
    i = 0
    while i <= 14:
        i += 1
        if i < 15:
            codeget = s.recv(10).decode('utf-8')
            codeList += codeget
        else:
            pass
    sign = ""
    listan = []
    for elem in codeList:
        if elem != " " or "":
            sign +=elem
        else:
            listan.append(sign)
            sign = ""
    return listan

def engMen(s, clientNr, data, lg):
    s.send(lg.encode('utf-8'))
    banner = s.recv(1024).decode('utf-8')
    print(banner)
    codeList = codeRecv(s)

    choice = input('Check amount (1)\nWithdraw cash (2)\nDeposit cash (3)\nByt språk (4)\nExit (5)\n')
    if choice != '5':
        #s.send(choice.encode('utf-8'))
        #f = open(clientNr, 'r')
        #amount = s.recv(1024).decode('utf-8')
        if choice == '1':
            s.send(choice.encode('utf-8'))
            amount = s.recv(1024).decode('utf-8')
            print ('Money left:  ' + amount)
            engMen(s, clientNr, data, lg)
        elif choice == '2':
            code = input('Enter safetycode: ')
            if code in codeList:
                s.send(choice.encode('utf-8'))
                amount = s.recv(1024).decode('utf-8')
                withdrawal = input('Enter amount to withdraw: ')
                withdrawal = str(int(withdrawal)*(-1))
                s.send(withdrawFunc(amount, withdrawal))
                engMen(s,clientNr, data, lg)
            else:
                choice = '1'
                s.send(choice.encode('utf-8'))
                amount = s.recv(1024).decode('utf-8')
                print('Wrong, please redo')
                engMen(s, clientNr, data, lg)
        elif choice == '3':
            s.send(choice.encode('utf-8'))
            amount = s.recv(1024).decode('utf-8')
            withdrawal = input('Enter amount to deposit: ')
            s.send(withdrawFunc(amount, withdrawal))
            engMen(s, clientNr, data, lg)
        elif choice == '4':
            s.send(choice.encode('utf-8'))
            s.recv(1024)
            language(s, clientNr, data)
        else:
            choice = 'wrong'
            s.send(choice.encode('utf-8'))
            amount = s.recv(1024).decode('utf-8')
            print('Not a valid choice, please try again!')
            engMen(s, clientNr, data, lg)
    else:
        return ("Thanks for visiting")
    s.close()

def withdrawFunc(a, w):
    a = str(int(a)+int(w))
    return a.encode('utf-8')



if __name__ == '__main__':
    Main()

