<?php

if (isset($_POST['camera'])) {
    switch ($_POST['camera'])
    {
    case "status":
        exec("vcgencmd get_camera", $ret, $status);
        //exec("vcgencmd get_camera | awk -F'=' '{print $3}'", $ret, $status);
        echo $ret;
        break;
    case "capture":
        exec("echo 0 > ".$attr_dir_prefix."led_attr/enable", $ret, $status);
        echo $status;
        break;
    case "uln2003-start":
        $process = popen("sudo ".$attr_dir_prefix."uln2003", "r");
        $ret = fgets($process, 100);
        echo $ret;
        pclose($process);
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
