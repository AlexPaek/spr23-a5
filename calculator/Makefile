objects = main.o multiplication.o addition.o division.o subtraction.o

calculator: $(objects) operations.h
	cc -o calculator $(objects)

$(objects): %.o:%.c operations.h
	cc -c $< -o $@

clean:
	rm -f calculator $(objects)

.PHONY: clean