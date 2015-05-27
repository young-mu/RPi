CC = gcc
DEBUG = -O3
INCLUDE = -I /usr/local/include
CFLAGS = $(DEBUG) -Wall $(INCLUDE) -Winline -pipe
LDFLAGS = -L /usr/local/lib
LDLIBS = -lwiringPi -lwiringPiDev -lpthread -lm

SRC = uln2003.c
OBJ = $(SRC:.c=.o)
BIN = $(SRC:.c=)

all:
	@echo "make [module]"
	@echo "module: $(BIN)"

uln2003: uln2003.o
	@echo [Link]
	@$(CC) -o $@ uln2003.o $(LDFLAGS) $(LDLIBS)

.c.o:
	@echo [Compile] $<
	@$(CC) -c $(CFLAGS) $< -o $@

clean:
	@echo [Clean]
	@rm -f $(OBJ) $(BIN)
