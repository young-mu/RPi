<?php

$uln2003_dir_prefix = "/srv/http/Controllers/C/";

if (isset($_POST['control'])) {
    switch ($_POST['control'])
    {
    case "uln2003-start":
        $process = popen("sudo ".$uln2003_dir_prefix."uln2003", "r");
        $ret = fgets($process, 100);
        echo $ret;
        pclose($process);
        break;
    case "uln2003-stop":
        exec("echo 0 > ".$uln2003_dir_prefix."uln2003_attr/enable", $ret, $status);
        echo $status;
        break;
    case "uln2003-turn":
        $direction = $_POST['direction'];
        exec("echo ".$direction." > ".$uln2003_dir_prefix."uln2003_attr/direction", $ret, $status);
        echo $status;
        break;
    case "uln2003-speed":
        $speed = $_POST['speed'];
        exec("echo ".$speed." > ".$uln2003_dir_prefix."uln2003_attr/speed", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
