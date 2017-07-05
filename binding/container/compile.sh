#!/bin/bash
g++ -c -fPIC container.cpp -o container.o
g++ -shared -Wl -o container.so  container.o
