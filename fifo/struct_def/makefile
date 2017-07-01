# Connor McCann

CC = gcc 
CFLAGS = -I.
OBJ = main.o string_fifo.o 

# rule to compile the executable if any of the source files are modified 
runMain: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

# rule to compile bits if its dependency or the file itself changes
string_fifo.o: string_fifo.c string_fifo.h
	$(CC) -c -o $@ string_fifo.c $(CFLAGS)

# rule to remove any .o file and the executable 
clean:
	-rm runMain main.o string_fifo.o 

# EOF
