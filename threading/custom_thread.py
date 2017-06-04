#!/Users/connormccann/anaconda/bin/python3.5
"""
	Program : Custom Working Threads
	Author  : Connor McCann
	Date    : 26 May 2017
	Source  : https://www.tutorialspoint.com/python/python_multithreading.htm
"""
import myThread 
import threading
import queue
import time
import math


# globals
exitFlag = 0
blocking = 1
queueLock = threading.Lock()
primeQueueLock = threading.Lock()
workQueue = queue.Queue(10000)
primeNumberResults = []

def find_primes(threadName, q):
	while not exitFlag:
		queueLock.acquire(blocking)
		if not workQueue.empty():
			num = q.get()
			queueLock.release()
			#print("%s processing %s" % (threadName, str(num)))
			is_prime(num)
		else:
			queueLock.release()

def is_prime(num):
	prime = True
	maxCheck = math.ceil(math.sqrt(num))+1
	for i in range(2,maxCheck):
		remainder = num % i
		if not remainder:
			prime = False
			break
	if (prime):
		primeQueueLock.acquire(blocking)
		primeNumberResults.append(num)
		primeQueueLock.release()


def main():
	threads = []
	threadID = 1

	# Create new threads
	for i in range(2):
		tName = "".join(("Thread-",str(i)))
		thread = myThread.myThread(threadID, tName, workQueue, find_primes)
		thread.start()
		threads.append(thread)
		threadID += 1

	# Fill the queue
	queueLock.acquire()
	for j in range(100000,110000):
		workQueue.put(j)
	queueLock.release()

	# Wait for queue to empty
	while not workQueue.empty():
		pass

	# Notify threads it's time to exit
	global exitFlag 
	exitFlag = 1

	# Wait for all threads to complete
	for t in threads:
		t.join()

	# Present the prime numbers found in non-decreasing order
	primeNumberResults.sort()
	print(primeNumberResults)
	print("Exiting Main Thread")

if __name__ == "__main__":
	main()
