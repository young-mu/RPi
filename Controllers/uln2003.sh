#!/bin/bash

# NOTE:
# this is the wrapper of uln2003.py, for now there exists time interval between speed switch, if want to avoid it, need to write step motor driver on kernel space.

function prUsage()
{
cat << EOF
Usage:
1) $0 start direction=[CW|CCW] speed=[1|2|3|4|5] (the higher the faster)
2) $0 stop
EOF
}

function clrUln2003()
{
    pid=`ps aux | grep "uln2003\.py" | awk '{print $2}'`
    if [ -n "$pid" ]; then
        kill -9 ${pid}
    fi
}

if [[ $# -ne 1 ]] && [[ $# -ne 3 ]]; then
    prUsage
elif [[ $# -eq 3 ]] && [[ $1 = "start" ]]; then
    if [[ $2 != "CW" ]] && [[ $2 != "CCW" ]]; then
        prUsage
    elif [[ $3 -lt 1 ]] || [[ $3 -gt 5 ]]; then
        prUsage
    else
        case $2 in
        "CW") direction=0;;
        "CCW") direction=1;;
        esac
        case $3 in
        1) delay=20;;
        2) delay=15;;
        3) delay=10;;
        4) delay=5;;
        5) delay=2;;
        esac
        clrUln2003
        ./uln2003.py start ${direction} ${delay} &
    fi
elif [[ $# -eq 1 ]] && [[ $1 = "stop" ]]; then
    clrUln2003
    ./uln2003.py stop
else
    prUsage
fi
