<?php

if (isset($_GET['camera'])) {
    switch ($_GET['camera'])
    {
    case "status":
        exec("/opt/vc/bin/vcgencmd get_camera | awk -F'=' '{print $3}'", $ret, $status);
        echo "$ret[0]";
        break;
    case "capture":
        $opt_resolution = $_GET['resolution'];
        $opt_quality = $_GET['quality'];
        $opt_encode = $_GET['encode'];
        $opt_flip = $_GET['flip'];
        $opt_delay = $_GET['delay'];
        $opt_name = $_GET['name'];
        exec("sudo /opt/vc/bin/raspistill $opt_resolution $opt_quality $opt_encode $opt_flip $opt_delay $opt_name", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
