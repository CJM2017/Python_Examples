#!/Users/connormccann/anaconda/bin/python
from ctypes import *


lib = cdll.LoadLibrary(myLibPath)

class Item(object):
    def __init__(self, obj):
        self.obj = obj
    def getName(self):
        return lib.Item_getName(self.obj)

class Container(object):
    def __init__(self):
        self.obj = lib.Container_init()

    def getItem(self,id):
        return lib.Container_getItem(self.obj,id)

lib.Item_getName.restype = c_char_p
lib.Item_getName.argtypes = ()

lib.Container_getItem.restype = Item
lib.Container_getItem.argtypes = [c_void_p,c_int]

c = Container()
print(c.getItem(5).getName())