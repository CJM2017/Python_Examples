"""
	Program : Synchronized Threads
	Author  : Connor McCann
	Date    : 26 May 2017
	Source  : https://www.tutorialspoint.com/python/python_multithreading.htm
"""
import threading


class myThread (threading.Thread):

	def __init__(self, threadID, name, q, func):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
		self.function = func

	def run(self):
		#print("Starting " + self.name)
		self.function(self.name, self.q)
		#print("Exiting " + self.name)