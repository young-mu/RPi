#!/bin/bash

# raspistill wrapper, since php cannot generate new file

PREFIX=/srv/http

/opt/vc/bin/raspistill $@ -o ${PREFIX}/image.jpg
