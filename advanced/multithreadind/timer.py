from threading import Thread
import time

def timer(name, delay, repeat):
    print "Timer: " + name + " Started"
    while repeat:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print "Timer: " + name + " Completed"

def Main():
    t1 = Thread(target = timer, args = ("Timer1", 1, 3))
    t2 = Thread(target = timer, args = ("Timer2", 1, 3))
    t1.start()
    t2.start()

    print "Main Completed"


if __name__ == '__main__':
    Main()