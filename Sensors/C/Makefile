CC = gcc
DEBUG = -O3
INCLUDE = -I /usr/local/include
CFLAGS = $(DEBUG) -Wall $(INCLUDE) -Winline -pipe
LDFLAGS = -L /usr/local/lib
LDLIBS = -lwiringPi -lwiringPiDev -lpthread -lm

SRC = sw420.c
OBJ = $(SRC:.c=.o)
BIN = $(SRC:.c=)

all:
	@echo "make [module]"
	@echo "module: $(BIN)"

sw420: sw420.o
	@echo [Link] $@
	@$(CC) -o $@ $< $(LDFLAGS) $(LDLIBS)
	@echo [Clean] $<
	@rm -f $<

.c.o:
	@echo [Compile] $<
	@$(CC) -c $(CFLAGS) $< -o $@

clean:
	@echo [Clean]
	@rm -f $(OBJ) $(BIN)
