import socket
import threading
import time

tLock = threading.Lock()
shutDown = False

def receving(name, sock):
    while not shutDown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except Exception as e:
            if str(e) == "[Errno 35] Resource temporarily unavailable":
                continue
            else:
                print e
        else:
            pass
        finally:
            pass

host = '127.0.0.1'

port = 0

server = ('127.0.0.1', 5000)

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + "->")
while message != 'q' and not shutDown:
    if message != '' :
        s.sendto(alias + ": " + message, server)
        time.sleep(0.2)
        message = raw_input(alias + "->")
    else:
        client_input = raw_input("end?     \n 'y' to quit\n 'n' to continue\n")
        if "y" in client_input:
            shutDown = True
        elif "n" in client_input:
            message = "reconnecting..."
        else:
            pass
rT.join()
        
s.close()
