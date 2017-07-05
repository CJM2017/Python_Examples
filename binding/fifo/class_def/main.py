#!/Users/connormccann/anaconda/bin/python3.5
#Source: https://stackoverflow.com/questions/19198872/how-do-i-return-objects-from-a-c-function-with-ctypes
import sys
from ctypes import *


# Global space
lib = cdll.LoadLibrary('./libstringfifo.so')

class Fifo(object):
    def __init__(self):
        self.obj = lib.new_fifo()

    def put(self, msg):
        lib.put(self.obj, msg)

lib.put.argtypes = [c_void_p, c_wchar_p]
lib.put.restype = None

def main():
    myFifo = Fifo()
    myFifo.put("Hello world")

if __name__ == "__main__":
    sys.exit(main())