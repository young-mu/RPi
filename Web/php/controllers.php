<?php

if (isset($_POST['control'])) {
    switch ($_POST['control'])
    {
    case "uln2003-start":
        exec("sudo /srv/http/Controllers/C/uln2003 &", $ret, $status);
        if ($status == 0) {
            echo "$ret[0]";
        } else {
            echo 1;
        }
        break;
    case "uln2003-stop":
        exec("sudo echo 0 > /srv/http/Controllers/C/uln2003_attr/enable", $ret, $status);
        echo $status;
        break;
    case "uln2003-turn":
        $direction = $_POST['direction'];
        exec("sudo echo " . $direction . " > /srv/http/Controllers/C/uln2003_attr/direction", $ret, $status);
        echo $status;
    case "uln2003-speed":
        $speed = $_POST['speed'];
        exec("sudo echo " . $speed . " > /srv/http/Controllers/C/uln2003_attr/speed", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
