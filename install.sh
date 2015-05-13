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

function apply()
{
    echo "OK"
}

function pDiff()
{
    if [ $# -eq 0 ]; then
        echo -e -n "1. Web/index.html\t\t"
        diff Web/index.html ${PREFIX}/index.html > /dev/null 2>&1
        retChk
        echo -e -n "2. Web/sensors.php\t\t"
        diff Web/sensors.php ${PREFIX}/sensors.php > /dev/null 2>&1
        retChk
        echo -e -n "3. Web/css\t\t\t"
        diff Web/css ${PREFIX}/css > /dev/null 2>&1
        retChk
        echo -e -n "4. Web/js\t\t\t"
        diff Web/js ${PREFIX}/js > /dev/null 2>&1
        retChk
        echo -e -n "5. Web/fonts\t\t\t"
        diff Web/fonts ${PREFIX}/fonts > /dev/null 2>&1
        retChk
        echo -e -n "6. Web/raw\t\t\t"
        diff Web/raw ${PREFIX}/raw > /dev/null 2>&1
        retChk
        echo -e -n "7. Sensors\t\t\t"
        diff Sensors ${PREFIX}/Sensors > /dev/null 2>&1
        retChk
        echo -e -n "8. Tools\t\t\t"
        diff Tools ${PREFIX}/Tools > /dev/null 2>&1
        retChk
    elif [ $# -eq 1 ]; then
        case "$1" in
            1) colordiff Web/index.html ${PREFIX}/index.html;;
            2) colordiff Web/sensors.php ${PREFIX}/sensors.php;;
            3) colordiff Web/css ${PREFIX}/css;;
            4) colordiff Web/js ${PREFIX}/js;;
            5) colordiff Web/fonts ${PREFIX}/fonts;;
            6) colordiff Web/raw ${PREFIX}/raw;;
            7) colordiff Sensors ${PREFIX}/Sensors;;
            8) colordiff Tools ${PREFIX}/Tools;;
        esac
    fi
}

if [[ $# -eq 1 ]] && [[ $1 = "diffall" ]]; then
    pDiff
elif [[ $# -eq 2 ]] && [[ $1 = "diff" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 8 ]]; then
        pDiff $2
    fi
elif [[ $# -eq 2 ]] && [[ $1 = "apply" ]]; then
    if [[ $2 -ge 1 ]] && [[ $2 -le 8 ]]; then
        apply $2
    fi
fi


