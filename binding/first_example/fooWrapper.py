#!/Users/connormccann/anaconda/bin/python3.5
import sys
from ctypes import cdll

# Global space
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

def main():
    f = Foo()
    f.bar()

if __name__ == "__main__":
    sys.exit(main())