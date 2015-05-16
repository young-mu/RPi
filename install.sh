#!/bin/bash

PREFIX="/srv/http"

function retChk()
{
    if [ $? = 0 ]; then
        echo -e "[\e[0;32m OK \e[0m]"
    else
        echo -e "[\e[0;31m FAIL \e[0m]"
    fi
}

function prUsage()
{
cat << EOF
Usage:
1) $0 diffall
2) $0 diff N
3) $0 apply N
EOF
}

function apply()
{
    case "$1" in
        1) cp Web/index.html ${PREFIX}/index.html;;
        2) cp Web/sensors.php ${PREFIX}/sensors.php;;
        3) rm -rf ${PREFIX}/css; cp -r Web/css ${PREFIX}/css;;
        4) rm -rf ${PREFIX}/js; cp -r Web/js ${PREFIX}/js;;
        5) rm -rf ${PREFIX}/fonts; cp -r Web/fonts ${PREFIX}/fonts;;
        6) rm -rf ${PREFIX}/raw; cp -r Web/raw ${PREFIX}/raw;;
        7) rm -rf ${PREFIX}/Sensors; cp -r Sensors ${PREFIX}/Sensors;;
        8) rm -rf ${PREFIX}/Tools; cp -r Tools ${PREFIX}/Tools;;
    esac
}

function prDiff()
{
    if [ $# -eq 0 ]; then
        echo -e -n "1. Web/index.html\t\t"
        diff Web/index.html ${PREFIX}/index.html > /dev/null 2>&1
        retChk
        echo -e -n "2. Web/sensors.php\t\t"
        diff Web/sensors.php ${PREFIX}/sensors.php > /dev/null 2>&1
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
    elif [ $# -eq 1 ]; then
        case "$1" in
            1) colordiff Web/index.html ${PREFIX}/index.html;;
            2) colordiff Web/sensors.php ${PREFIX}/sensors.php;;
            3) colordiff -r Web/css ${PREFIX}/css;;
            4) colordiff -r Web/js ${PREFIX}/js;;
            5) colordiff -r Web/fonts ${PREFIX}/fonts;;
            6) colordiff -r Web/raw ${PREFIX}/raw;;
            7) colordiff -r Sensors ${PREFIX}/Sensors;;
            8) colordiff -r Tools ${PREFIX}/Tools;;
        esac
    fi
}

if [[ $# -eq 0 ]]; then
    prUsage
elif [[ $# -eq 1 ]] && [[ $1 = "diffall" ]]; then
    prDiff
elif [[ $# -eq 2 ]] && [[ $1 = "diff" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 8 ]]; then
        prDiff $2
    else
        prUsage
    fi
elif [[ $# -eq 2 ]] && [[ $1 = "apply" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 8 ]]; then
        apply $2
    else
        prUsage
    fi
else
    prUsage
fi
