import threading
import time

class AsyncWrite(threading.Thread):
    """docstring for AsyncWrite"""
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print "file written to " + self.out

def Main():
    message = raw_input("input a string to store:")
    write = AsyncWrite(message, 'out.text')
    write.start()
    print "processing..."
    write.join()
    print "process completed"

if __name__ == '__main__':
    Main()
        