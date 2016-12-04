import socket
import threading
import os

def RetrFile(name, sock):
    filename = sock.recv(1024)
    filename.decode('utf-8')
    print(filename)
    if os.path.isfile(filename):
        msg = b'Exists'
        #sock.send(msg.encode('utf-8'))
        sock.send(b'Exists')
        while True:
            lang = sock.recv(1024).decode('utf-8')
            print(lang +"---------------------")
            if lang == '1':
                f = open('banner.txt', 'r')
                bannermsg = f.read()
                print(len(bannermsg))
                if len(bannermsg) > 80:
                    bannermsg = '%%%%%%%%%%%%%%%%%%%%'
                else:
                    bannermsg = bannermsg
                sock.send(bannermsg.encode('utf-8'))
            else:
                f = open('bannerEng.txt', 'r')
                bannermsg = f.read()
                if len(bannermsg) > 80:
                    bannermsg = '%%%%%%%%%%%%%%%%%%%%%%'
                else:
                    bannermsg = bannermsg
                sock.send(bannermsg.encode('utf-8'))
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

            sock.send(codeList.encode('utf-8'))
            menuChoice = sock.recv(1024).decode('utf-8')
            #menuChoice.decode('utf-8')
            #while menuChoice:
            if menuChoice != 'wrong':
                f = open(filename, 'r')
                amount = f.read(1024)
                f.close()
                sock.send(amount.encode('utf-8'))
                #f = open(filename, 'w')
                #f.write(amount)
                #f.close()
                newAmount = amount

                if menuChoice in ['2','3']:
                    print("hej")
                    newAmount = sock.recv(1024).decode('utf-8')
                if newAmount != "":
                    f = open(filename, 'w')
                    print (newAmount+ '   ---------')
                    f.write(newAmount)
                    f.close()
                else:
                    print('no input')
            else:
                pass
    else:
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
