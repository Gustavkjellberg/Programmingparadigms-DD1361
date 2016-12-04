import socket
import threading


tLock = threading.Lock()
shutdown = False



def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                data = data.decode('utf-8')
                print(data + "----")
        except:
            pass
        finally:
            tLock.release()

host = '127.0.0.1'
port = 0

server = (host, 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

alias = "Customer:   "
message = input("Svenska (1)\nEnglish(2)\nQuit(3)\n\n")
#message = input()

while message != 'q':
    if message == '4':
        s.sendto(alias.encode('utf-8') + b": " +message.encode('utf-8'), server)  #här blir datan även client
        s.close()
    elif message != '':
        s.sendto(alias.encode('utf-8') + b": " +message.encode('utf-8'), server)  #här blir datan även client
        tLock.acquire()
        message = input(alias + "-> ")
        tLock.release()
        #kolla detta, kanske är anledningen till att det ligger i en cp loop där den börjar från början
shutdown = True

rT.join()
s.close()




if menuChoice != '4':
    f = open(filename, 'r')
    amount = f.read(1024)
    f.close()
    sock.send(amount.encode('utf-8'))
    print(menuChoice)
    if menuChoice == '1':
        #f = open(filename, 'w')
        #f.write(amount)
        #f.close()
        newAmount = amount
    elif menuChoice == '2' or '3':
        newAmount = sock.recv(1024).decode('utf-8')
    if newAmount != "":
        f = open(filename, 'w')
        print (newAmount+ '   ---------')
        f.write(newAmount)
        f.close()