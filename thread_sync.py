#!/Users/connormccann/anaconda/bin/python3.5
"""
    Program : Synchronized Threads
    Author  : Connor McCann
    Date    : 26 May 2017
    Source  : https://www.tutorialspoint.com/python/python_multithreading.htm
"""
import threading
import time

# globals
# if these were defined within main the threads
# would not have accessed
threadLock = threading.Lock()
blocking = 1 

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # get the lock to sync threads
        threadLock.acquire(blocking)
        print_time(self.name, self.counter, 3)
        # free the lock to release next thread
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def main():
    # array to manage threads
    threads = []
    
    # create new threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # start new threads
    # start method starts thread by calling run method
    thread1.start()
    thread2.start()

    # Add threads to the the thread list
    threads.append(thread1)
    threads.append(thread2)

    # wait for all threads to complete
    for t in threads:
        t.join() # the join() waits for threads to terminate
    print("Exiting main Thread")

if __name__ == "__main__":
    main()

"""
    Starting Thread-1
    Starting Thread-2
    Thread-1: Sat May 27 13:31:36 2017
    Thread-1: Sat May 27 13:31:37 2017
    Thread-1: Sat May 27 13:31:38 2017
    Thread-2: Sat May 27 13:31:40 2017
    Thread-2: Sat May 27 13:31:42 2017
    Thread-2: Sat May 27 13:31:44 2017
    Exiting main Thread
"""
