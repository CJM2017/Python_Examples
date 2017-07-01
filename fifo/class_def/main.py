#!/Users/connormccann/anaconda/bin/python3.5
import sys
from ctypes import cdll


# Global space
lib = cdll.LoadLibrary('./libstringfifo.so')

class Fifo(object):
    def __init__(self):
        self.obj = lib.new_fifo()

    def put(self, msg):
        lib.put(self.obj, msg)

def main():
    myFifo = Fifo()
    #myFifo.put("Hello world")

if __name__ == "__main__":
    sys.exit(main())