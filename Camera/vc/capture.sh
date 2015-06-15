#!/bin/bash

# raspistill wrapper, since php cannot generate new file

PREFIX=/srv/http

FILETYPE=${8}
/opt/vc/bin/raspistill $@ -o ${PREFIX}/image.${FILETYPE}
