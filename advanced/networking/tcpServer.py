import socket

def Main():
    host = '127.0.0.1'
    port = 8080

    s = socket.socket()
    s.bind((host, port))

    s.listen(10)

    c, addr = s.accept()
    print "Connection from : " + str(addr)

    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        print "send:" + str(data)
        c.send(data)

    c.close()

if __name__ == '__main__':
    Main()