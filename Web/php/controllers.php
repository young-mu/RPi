<?php

$uln2003_dir_prefix = "/srv/http/Controllers/C/";

if (isset($_POST['control'])) {
    switch ($_POST['control'])
    {
    case "uln2003-start":
        exec("sudo ".$uln2003_dir_prefix."uln2003 &", $ret, $status);
        if ($status == 0) {
            echo "$ret[0]";
        } else {
            echo 1;
        }
        break;
    case "uln2003-stop":
        exec("sudo echo 0 > ".$uln2003_dir_prefix."uln2003_attr/enable", $ret, $status);
        echo $status;
        break;
    case "uln2003-turn":
        $direction = $_POST['direction'];
        exec("sudo echo ".$direction." > ".$uln2003_dir_prefix."uln2003_attr/direction", $ret, $status);
        echo $status;
    case "uln2003-speed":
        $speed = $_POST['speed'];
        exec("sudo echo ".$speed." > ".$uln2003_dir_prefix."uln2003_attr/speed", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
