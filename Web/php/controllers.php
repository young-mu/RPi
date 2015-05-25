<?php

if (isset($_POST['controller'])) {
    switch ($_POST['controller'])
    {
    case "uln2003-start":
        exec("sudo ./Controllers/uln2003.py start", $ret, $status);
        echo $status;
        break;
    case "uln2003-stop":
        exec("sudo ./Controllers/uln2003.py start", $ret, $status);
        echo $status;
        break;
    case "uln2003-speedup":
        exec("sudo ./Controllers/uln2003.py start", $ret, $status);
        echo $status;
        break;
    case "uln2003-speeddown":
        exec("sudo ./Controllers/uln2003.py start", $ret, $status);
        echo $status;
        break;
    default:
        echo "default";
    }
} else {
    echo "Error";
}

?>
