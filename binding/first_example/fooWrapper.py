#!/Users/connormccann/anaconda/bin/python
import sys
from ctypes import *


# Global space
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def show_num(self):
        #return cast(lib.Foo_num(self.obj), py_object).value
        return lib.Foo_num(self.obj)

lib.Foo_num.argtypes = [c_void_p]
lib.Foo_num.restype = c_int

def main():
    f = Foo()
    f.bar()
    f.show_num()

if __name__ == "__main__":
    sys.exit(main())