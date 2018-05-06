import socket
import time

#main
def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    language(s)


#Client chooses language and types in log-in details
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

        sender(s, clientNr)
        data = reciver(s)
        sender(s, clientCode)
        passOk = reciver(s)
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

#swedish menu
def sweMen(s, clientNr, data, lg):
    sender(s, lg)
    banner = reciver(s)
    print(banner)
    codeList = codeRecv(s)
    choice = input('Saldo (1)\nTa ut pengar (2)\nSätt in pengar (3)\nChange language (4)\nAvsluta (5)\n')
    if choice != '5':
        if choice == '1':
            sender(s, choice)
            amount = reciver(s)
            print ('Saldo:  ' + amount)
            sweMen(s, clientNr, data, lg)
        elif choice == '2':
            code = input('Ange säkerhetskod: ')
            print (codeList[0]+ "-------")
            for okCode in codeList:
                print (okCode)
                if okCode == code:

                    sender(s, choice)
                    amount = reciver(s)
                    withdrawal = input('Ange summa att ta ut: ')
                    withdrawal = str(int(withdrawal)*(-1))
                    w = withdrawFunc(amount,withdrawal)
                    sender(s, w)
                    sweMen(s,clientNr, data, lg)
            choice = '1'
            sender(s, choice)
            amount = reciver(s)
            print('Fel, vänligen gör om')
            sweMen(s, clientNr, data, lg)
        elif choice == '3':
            sender(s, choice)
            amount = reciver(s)
            withdrawal = input('Hur  mycket ill du sätta in?: ')
            w = withdrawFunc(amount, withdrawal)
            sender(s, w)
            sweMen(s, clientNr, data, lg)
        elif choice == '4':
            sender(s, choice)
            reciver(s)
            language(s, clientNr, data)
        else:
            choice = 'wrong'
            sender(s, choice)
            amount = reciver(s)
            print('Ej ett giltligt val, försök igen!')
            sweMen(s, clientNr, data, lg)
    else:
        return ('Tack för besöket!')
    s.close()

#Sends packages with size 10 bytes
def sender(sock, msg):
    print(msg)
    msg += 'q'
    while len(msg)>10:
        sock.send(msg[0:10].encode('utf-8'))
        msg = msg[10:]
    if len(msg) == 10:
        sock.send(msg.encode('utf-8'))
    elif len(msg) > 0:
        sock.send(msg.encode('utf-8'))


#Recives 10 bytes in each package, continues until everything is recived
def reciver(s):
    fullMsg = ""
    while True:
        data = s.recv(10).decode('utf-8')
        fullMsg += data
        if 'q' in data:
            break

    return (fullMsg[0:len(fullMsg)-1])

#ivides string into smaller pieces and puts each piece in a list
def codeRecv(s):
    codeList = reciver(s)
    listan = []
    sign = ""
    for elem in codeList:
        if elem != 'q':
            if elem != ' ':
                sign +=elem
            else:
                listan.append(sign)
                sign = ""

    return listan

#English menu
def engMen(s, clientNr, data, lg):
    sender(s, lg)
    banner = reciver(s)
    print(banner)
    codeList = codeRecv(s)
    choice = input('Check amount (1)\nWithdraw cash (2)\nDeposit cash (3)\nByt språk (4)\nExit (5)\n')
    if choice != '5':
        if choice == '1':
            sender(s, choice)
            amount = reciver(s)
            print ('balance:  ' + amount)
            engMen(s, clientNr, data, lg)
        elif choice == '2':
            code = input('Safeteycode: ')
            print (codeList[0]+ "-------")
            for okCode in codeList:
                print (okCode)
                if okCode == code:

                    sender(s, choice)
                    amount = reciver(s)
                    withdrawal = input('Enter amount to withdraw: ')
                    withdrawal = str(int(withdrawal)*(-1))
                    w = withdrawFunc(amount,withdrawal)
                    sender(s, w)
                    engMen(s,clientNr, data, lg)
            choice = '1'
            sender(s, choice)
            amount = reciver(s)
            print('Wrong, please redo')
            engMen(s, clientNr, data, lg)
        elif choice == '3':
            sender(s, choice)
            amount = reciver(s)
            withdrawal = input('Enter amount to deposit?: ')
            w = withdrawFunc(amount, withdrawal)
            sender(s, w)
            engMen(s, clientNr, data, lg)
        elif choice == '4':
            sender(s, choice)
            reciver(s)
            language(s, clientNr, data)
        else:
            choice = 'wrong'
            sender(s, choice)
            amount = reciver(s)
            print('Invalid choice, try again!')
            engMen(s, clientNr, data, lg)
    else:
        return ('Thanks for using ATM!')
    s.close()

#updates balance
def withdrawFunc(a, w):
    a = str(int(a)+int(w))
    return a

if __name__ == '__main__':
    Main()

