#!/bin/bash

echo "1. Web/index.html"
diff Web/index.html /srv/http/index.html
echo "2. Web/sensors.php"
diff Web/sensors.php /srv/http/sensors.php
echo "3. Web/css"
diff Web/css /srv/http/css
echo "4. Web/js"
diff Web/js /srv/http/js
echo "5. Web/fonts"
diff Web/fonts /srv/http/fonts
echo "6. Web/raw"
diff Web/raw /srv/http/raw
echo "7. Sensors"
diff Sensors /srv/http/Sensors
echo "8. Tools"
diff Tools /srv/http/Tools
