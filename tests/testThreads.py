'''they say thread is a low level library, you should use threading.'''
import time
import thread
from threading import Thread
import sys
STDERR = sys.stderr
def excepthook(*args):
    print >> STDERR,"cauht exception"
    print >> STDERR,args
#sys.excepthook = excepthook
def timer(no,interval):
    cnt = 0
    while cnt < 10:
        print "thread no :%d time $s"% no,time.ctime()
        time.sleep(interval)
        cnt += 1

def test():
    print  "hello"
    try:
        thread.start_new_thread(timer,(1,1))
        thread.start_new_thread(timer, (2, 2))
    except:
        pass

def testThreading():
    t1 = Thread(target=timer,args=(1,1))
    t2 = Thread(target=timer,args=(2,2))
    t1.start()
    t2.start()

if __name__=='__main__':
    # test()
    testThreading()

