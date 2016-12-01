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
                print(data)
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

alias = input("Name: ")
message = input(alias + "-> ")

while message != 'q':
    if message != '':
        s.sendto(alias.encode('utf-8') + b": " +message.encode('utf-8'), server)
        tLock.acquire()
        message = input(alias + "-> ")
        tLock.release()

shutdown = True

rT.join()
s.close()







"""def Main():

    host = '127.0.0.1'
    port = 5001

    server = ((host, 5000))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-> ")

    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recivied form server: " + data)
        message = input("-> ")

    s.close()



if __name__ == '__main__':
    Main()"""