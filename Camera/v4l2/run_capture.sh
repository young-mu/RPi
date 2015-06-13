#!/bin/bash

SRC=./capture.c
BIN=capture

# compile capture.c
echo "compile $SRC"
gcc $SRC -lv4l2 -o $BIN

# run the program
echo "run $BIN"
./$BIN output.ppm 320 240
