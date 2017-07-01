#!/usr/bin/python3.5

import sys
import unittest
import subprocess as sp
import os


class TestFIFO(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestFIFO, cls).setUpClass()	# http://www.pythonforbeginners.com/super/working-python-super-function

    def testDefaultQueueSize(self):
    	pass

if __name__ == "__main__":
    sys.exit(unittest.main())