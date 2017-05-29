#!/usr/bin/python3.5
import sys

class UAV: # will always take one argument (self)

	numVehicles = 0; # this is a static class variable

	def __init__(self,numMotors,frameType): # the class constructor which contains all member varsS
		self.motors = numMotors
		self.frameType = frameType
		UAV.numVehicles  += 1
		print('Just made a UAV')

	def displayInfo(self):
		print('The vehicle has ' + str(self.motors) + ' motors')
		print('The vehicle is off frame type: ' + self.frameType)
		print('Number of UAV instances: ' + str(UAV.numVehicles))


def main():
	
	quad1 = UAV(4,'X')
	quad1.displayInfo()

	quad2 = UAV(6,'Hexa')
	quad2.displayInfo()

	quad2 = UAV(8,'Octa')
	quad2.displayInfo()

if __name__ == '__main__':
	sys.exit(main())