#!/Users/connormccann/anaconda/bin/python3.5
"""
Program : Synchronized Threads
Author  : Connor McCann
Date    : 26 May 2017
Source  : https://www.tutorialspoint.com/python/python_multithreading.htm
"""
import queue
import threading
import time


# globals
exitFlag = 0
queueLock = threading.Lock()
workQueue = queue.Queue(10)

class myThread (threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		print("Starting " + self.name)
		process_data(self.name, self.q)
		print("Exiting " + self.name)

def process_data(threadName, q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()
			queueLock.release()
			print("%s processing %s" % (threadName, data))
		else:
			queueLock.release()
		time.sleep(1) # 1 second pause

def main():
	threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5"]
	nameList = ["One", "Two", "Three", "Four", "Five","siz","seven","eight","nine","ten"]
	threads = []
	threadID = 1

	# Create new threads
	for tName in threadList:
		thread = myThread(threadID, tName, workQueue)
		thread.start()
		threads.append(thread)
		threadID += 1

	# Fill the queue
	queueLock.acquire()
	for word in nameList:
		workQueue.put(word)
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
	print("Exiting Main Thread")

if __name__ == "__main__":
	main()
