<?php

if (isset($_POST['sensor'])) {
    switch ($_POST['sensor'])
    {
    case "bcm2836-cputemp":
        exec("sudo ./Tools/getTemp.py", $ret, $status);
        if ($status == 0) {
            echo "$ret[0]";
        } else {
            echo 0;
        }
        break;
    case "bcm2836-gputemp":
        exec("sudo ./Tools/getTemp.py", $ret, $status);
        if ($status == 0) {
            echo "$ret[1]";
        } else {
            echo 0;
        }
        break;
    case "dht11-hum":
        exec("sudo ./Sensors/dht11.py", $ret, $status);
        if ($status == 0) {
            echo "$ret[0]";
        } else {
            echo 0;
        }
        break;
    case "dht11-temp":
        exec("sudo ./Sensors/dht11.py", $ret, $status);
        if ($status == 0) {
            echo "$ret[1]";
        } else {
            echo 0;
        }
        break;
    case "bh1750":
        exec("sudo ./Sensors/bh1750.py", $ret, $status);
        if ($status == 0) {
            echo "$ret[0]";
        } else {
            echo 0;
        }
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
