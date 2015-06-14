# RPi
all projects of RaspberryPi2

__Projects__

* Tools/getTemp.py: get CPU & GPU temperature
* Tools/sendMail.py: send email by SMTP protocol
* Tools/getAQI.py: get shanghai Air Quality Index
* Tools/getWeather.py: get weather now and following 7 day forecasts
* Sensors/dht11.py: get humidity & temperature
* Sensors/ds18b20.py: get temperature (NOT test)
* Sensors/sw420.py: get vibration trigger
* Sensors/bh1750.py: get light intensivity
* Controllers/C/led: control led
* Controllers/C/uln2003: control step motor
* (experimental)Camera/opencv/capture.c: take a photo using opencv (support USB camera only for now)
* (experimental)Camera/v4l2/capture.c: take a photo using v4l2
* Camera/vc/capture.sh: take a photo using broadcom firmware
* Web: (based on 3.3.4 bootstrap and 2.1.3 jQuery)

__Bugs__
* when changing uln2003 speed, sometimes it will crash (it may be module internal bug)

__TODO list__
* improve install.sh (one source)
* rewrite Controllers (led/uln2003) driver (abandon wiringPi user lib)
* support homepage menu auto close in iPhone
* support CSI raspberrypi camera on opencv
* complete download button event
