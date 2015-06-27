#!/bin/bash

PREFIX="/srv/http" # on RPi for run
#PREFIX="/Library/WebServer/Documents" # on Mac for development
#PREFIX="/run/www/html" # on Ubuntu for development

function retChk()
{
    if [ $? = 0 ]; then
        echo -e "[\033[0;32m OK \033[0m]"
    else
        echo -e "[\033[0;31m FAIL \033[0m]"
    fi
}

function prUsage()
{
cat << EOF
Usage:
1) $0 diffall
2) $0 diff N
3) $0 applyall
4) $0 apply N
EOF
}

function apply()
{
    if [ $# -eq 0 ]; then
        echo "------------- [applyall] -------------"
        rm -rf ${PREFIX}/*
        echo -e -n "1. Web/index/html\t\t"
        cp Web/index.html ${PREFIX}/index.html
        retChk
        echo -e -n "2. Web/php\t\t\t"
        rm -rf ${PREFIX}/php; cp -r Web/php ${PREFIX}/php
        retChk
        echo -e -n "3. Web/css\t\t\t"
        rm -rf ${PREFIX}/css; cp -r Web/css ${PREFIX}/css
        retChk
        echo -e -n "4. Web/js\t\t\t"
        rm -rf ${PREFIX}/js; cp -r Web/js ${PREFIX}/js
        retChk
        echo -e -n "5. Web/fonts\t\t\t"
        rm -rf ${PREFIX}/fonts; cp -r Web/fonts ${PREFIX}/fonts
        retChk
        echo -e -n "6. Web/raw\t\t\t"
        rm -rf ${PREFIX}/raw; cp -r Web/raw ${PREFIX}/raw
        retChk
        echo -e -n "7. Sensors\t\t\t"
        rm -rf ${PREFIX}/Sensors; cp -r Sensors ${PREFIX}/Sensors
        retChk
        echo -e -n "8. Tools\t\t\t"
        rm -rf ${PREFIX}/Tools; cp -r Tools ${PREFIX}/Tools
        retChk
        echo -e -n "9. Controllers\t\t\t"
        rm -rf ${PREFIX}/Controllers; cp -a Controllers ${PREFIX}/Controllers
        retChk
        echo -e -n "10. Camera\t\t\t"
        rm -rf ${PREFIX}/Camera; cp -a Camera ${PREFIX}/Camera
        retChk
    elif [ $# -eq 1 ]; then
        case $1 in
            1) cp Web/index.html ${PREFIX}/index.html;;
            2) rm -rf ${PREFIX}/php; cp -r Web/php ${PREFIX}/php;;
            3) rm -rf ${PREFIX}/css; cp -r Web/css ${PREFIX}/css;;
            4) rm -rf ${PREFIX}/js; cp -r Web/js ${PREFIX}/js;;
            5) rm -rf ${PREFIX}/fonts; cp -r Web/fonts ${PREFIX}/fonts;;
            6) rm -rf ${PREFIX}/raw; cp -r Web/raw ${PREFIX}/raw;;
            7) rm -rf ${PREFIX}/Sensors; cp -r Sensors ${PREFIX}/Sensors;;
            8) rm -rf ${PREFIX}/Tools; cp -r Tools ${PREFIX}/Tools;;
            9) rm -rf ${PREFIX}/Controllers; cp -a Controllers ${PREFIX}/Controllers;;
            10) rm -rf ${PREFIX}/Camera; cp -a Camera ${PREFIX}/Camera;;
        esac
    fi
}

function prDiff()
{
    if [ $# -eq 0 ]; then
        echo "------------- [diffall] -------------"
        echo -e -n "1. Web/index.html\t\t"
        diff Web/index.html ${PREFIX}/index.html > /dev/null 2>&1
        retChk
        echo -e -n "2. Web/php\t\t\t"
        diff -r Web/php ${PREFIX}/php > /dev/null 2>&1
        retChk
        echo -e -n "3. Web/css\t\t\t"
        diff -r Web/css ${PREFIX}/css > /dev/null 2>&1
        retChk
        echo -e -n "4. Web/js\t\t\t"
        diff -r Web/js ${PREFIX}/js > /dev/null 2>&1
        retChk
        echo -e -n "5. Web/fonts\t\t\t"
        diff -r Web/fonts ${PREFIX}/fonts > /dev/null 2>&1
        retChk
        echo -e -n "6. Web/raw\t\t\t"
        diff -r Web/raw ${PREFIX}/raw > /dev/null 2>&1
        retChk
        echo -e -n "7. Sensors\t\t\t"
        diff -r Sensors ${PREFIX}/Sensors > /dev/null 2>&1
        retChk
        echo -e -n "8. Tools\t\t\t"
        diff -r Tools ${PREFIX}/Tools > /dev/null 2>&1
        retChk
        echo -e -n "9. Controllers\t\t\t"
        diff -r Controllers ${PREFIX}/Controllers > /dev/null 2>&1
        retChk
        echo -e -n "10. Camera\t\t\t"
        diff -r Camera ${PREFIX}/Camera > /dev/null 2>&1
        retChk
    elif [ $# -eq 1 ]; then
        case $1 in
            1) colordiff Web/index.html ${PREFIX}/index.html;;
            2) colordiff -r Web/php ${PREFIX}/php;;
            3) colordiff -r Web/css ${PREFIX}/css;;
            4) colordiff -r Web/js ${PREFIX}/js;;
            5) colordiff -r Web/fonts ${PREFIX}/fonts;;
            6) colordiff -r Web/raw ${PREFIX}/raw;;
            7) colordiff -r Sensors ${PREFIX}/Sensors;;
            8) colordiff -r Tools ${PREFIX}/Tools;;
            9) colordiff -r Controllers ${PREFIX}/Controllers;;
            10) colordiff -r Camera ${PREFIX}/Camera;;
        esac
    fi
}

if [[ $# -eq 0 ]]; then
    prUsage
elif [[ $# -eq 1 ]] && [[ $1 = "diffall" ]]; then
    prDiff
elif [[ $# -eq 1 ]] && [[ $1 = "applyall" ]]; then
    apply
elif [[ $# -eq 2 ]] && [[ $1 = "diff" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 10 ]]; then
        prDiff $2
    else
        prUsage
    fi
elif [[ $# -eq 2 ]] && [[ $1 = "apply" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 10 ]]; then
        apply $2
    else
        prUsage
    fi
else
    prUsage
fi
