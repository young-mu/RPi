<?php

if (isset($_POST['camera'])) {
    switch ($_POST['camera'])
    {
    case "status":
        exec("/opt/vc/bin/vcgencmd get_camera | awk -F'=' '{print $3}'", $ret, $status);
        echo "$ret[0]";
        break;
    case "capture":
        $opt_resolution = $_POST['resolution'];
        $opt_quality = $_POST['quality'];
        $opt_encode = $_POST['encode'];
        $opt_flip = $_POST['flip'];
        $opt_delay = $_POST['delay'];
        exec("sudo /srv/http/Camera/vc/capture.sh $opt_resolution $opt_quality $opt_encode $opt_flip $opt_delay", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
