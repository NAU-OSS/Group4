# make file
func1: main.o
	gcc -o func1 main.o -L. -lfunc1

# object code for main.c
main.o: main.cpp func1.h
	gcc -c main.cpp func1.h

# target to clean up, removing anything that is not source code
clean:
	rm -f *.o *.a *.gch
