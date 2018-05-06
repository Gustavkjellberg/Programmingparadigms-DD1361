#Gustav Kjellberg 951028-2578
#Isak Hassbring 940204-1496
import socket
import threading
import os


#Recives 10 bytes in each package, continues until everything is recived
def reciver(s):
    fullMsg = ""
    while True:
        data = s.recv(10).decode('utf-8')
        fullMsg += data
        if 'q' in data:
            break

    print(fullMsg)
    return (fullMsg[0:len(fullMsg)-1])

#Sends packages with size 10 bytes
def sender(sock, msg):
    msg += 'q'
    while len(msg)>10:
        sock.send(msg[0:10].encode('utf-8'))
        msg = msg[10:]
    if len(msg) == 10:
        sock.send(msg.encode('utf-8'))
    elif len(msg) > 0:
        sock.send(msg.encode('utf-8'))




#Retrives client info, returns whatever client needs
def RetrFile(name, sock):
    filename = reciver(sock)+'.txt'
    print(filename)
    if os.path.isfile(filename):
        msg = 'Exists'
        sender(sock,msg)
        code = reciver(sock)
        f = open(filename, 'r')
        info = f.readlines()
        f.close()
        f = open(filename, 'w')
        print(info[0])
        f.write(info[0]+info[1])
        f.close()
        if code == info[0].strip():
            print ("HEJ")
            sender(sock, info[0])
        else:
            passer = 'noPass'
            sender(sock, passer)
        newAmount = info[1]

        while True:
            lang = reciver(sock)
            print(lang +"---------------------")
            if lang == '1':
                f = open('banner.txt', 'r')
                bannermsg = f.read()
                if len(bannermsg) > 80:
                    print("För långt meddelande... det är: " + str(len(bannermsg)) + " tecken")
                    bannermsg = 'WELCOME!!!'
                else:
                    bannermsg = bannermsg
                sender(sock, bannermsg)
            else:
                f = open('bannerEng.txt', 'r')
                bannermsg = f.read()
                if len(bannermsg) > 80:
                    print("To long msg... it's: " + str(len(bannermsg)) + " signs")
                    bannermsg = 'WELCOME'
                else:
                    bannermsg = bannermsg
                sender(sock, bannermsg)
            codeList = '01 '+'03'+ ' 05'+' 07'+' 09' \
                        ' 11'+ ' 13'+ ' 15' +' 17'+' 19' \
                        ' 21'+ ' 23'+ ' 25'+' 27'+' 29' \
                        ' 31'+ ' 33'+ ' 35'+' 37'+' 39' \
                        ' 41'+ ' 43'+ ' 45'+' 47'+' 49' \
                        ' 51'+ ' 53'+ ' 55'+' 57'+' 59' \
                        ' 61'+ ' 63'+ ' 65'+' 67'+' 69' \
                        ' 71'+ ' 73'+ ' 75'+' 77'+' 79' \
                        ' 81'+ ' 83'+ ' 85'+' 87'+' 89' \
                        ' 91'+ ' 93'+ ' 95'+' 97'+' 99 '

            sender(sock, codeList)
            menuChoice = reciver(sock)
            #menuChoice = sock.recv(1024).decode('utf-8')
            if menuChoice != 'wrong':
                f = open(filename, 'r')
                info = f.readlines()
                f.close()
                newAmount = info[1]
                sender(sock, info[1])
                if menuChoice in ['2','3']:
                    print("hej")
                    newAmount = reciver(sock)
                if newAmount != "":
                    f = open(filename, 'w')
                    print (newAmount+ '   ---------')
                    f.write(info[0] + newAmount)
                    f.close()
                else:
                    print('no input')
            else:
                pass
    else:
        msg = 'Error'
        sender(sock, msg)
    sock.close()
#main
def Main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    print('Server started...')

    while True:
        try:
            c, addr = s.accept()
            print('Client connected:   ' + str(addr))
            t = threading.Thread(target = RetrFile, args = ("retrThread", c))
            t.start()
        except socket.error:
            print("Client disconnected:    " + str(addr))
            s.close()

if __name__ == '__main__':
    Main()
