#!/bin/bash
g++ -c -fPIC string_fifo.cpp -o string_fifo.o
g++ -shared -Wl,-soname,libstringfifo.so -o libstringfifo.so  string_fifo.o
