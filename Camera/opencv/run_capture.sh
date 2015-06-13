#!/bin/bash

SRC=./capture.c
BIN=capture

# compile capture.c
echo "compile $SRC"
g++ -I /usr/include/opencv2/ `pkg-config --cflags --libs opencv` $SRC -o $BIN

# run the program
echo "run $BIN"
./$BIN
