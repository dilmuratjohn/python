import socket

def Main():
    host = '127.0.0.1'
    port = 8081

    server = ('127.0.0.1', 8080)

    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.bind((host, port))

    print "Client Started."

    message = raw_input("-> ")

    while message != 'q':
        c.sendto(message, server)
        data, addr = c.recvfrom(1024)
        print "message from: " + str(addr)
        print "Recieved from server: " + str(data)
        message = raw_input("-> ")
        
    c.close()

if __name__ == '__main__':
    Main()