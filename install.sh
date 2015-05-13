#!/bin/bash

function retChk()
{
    if [ $? = 0 ]; then
        echo -e "[\e[0;32m OK \e[0m]"
    else
        echo -e "[\e[0;31m FAIL \e[0m]"
    fi
}

PREFIX="/srv/http"

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
