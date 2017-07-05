#!/bin/bash

# Compile
make

# Format new lines
printf "\n\n"

# Run test file
./runMain

# Need to add the ability to only run the program 
# if the make is successful which means i need an echo
# or program exit condition of some kind
