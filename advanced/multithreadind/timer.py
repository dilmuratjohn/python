import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print "Timer" + name + ": Started."
    tLock.acquire()
    print "Timer" + name + ": has acquire the lock."
    while repeat > 0:
        time.sleep(delay)
        print "Timer" + name + ": " + str(time.ctime(time.time()))
        repeat -= 1
	print "Timer" + name + ": is releasing the lock."
	tLock.release()
	print "Timer" + name + ": Completed."

def Main():
    t1 = threading.Thread(target = timer, args = ("1", 1, 3))
    t2 = threading.Thread(target = timer, args = ("2", 2, 3))
    t1.start()
    t2.start()

    print "Main Completed."


if __name__ == '__main__':
    Main()
