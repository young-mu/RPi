var php_exec = "/php/controllers.php";
var led_ebl = 0;
var uln2003_ebl = 0;
var uln2003_dir = 0;
var uln2003_spd = 1;

$(document).ready(function() {
    $("#led-open").click(function() {
        if (led_ebl == 1) {
            console.log("already opened!");
        } else {
            $.ajax({
                type: "POST",
                url: php_exec,
                async: false,
                data: {control:"led-open"},
                success: function(ret) {
                    if (ret != 1) {
                        var data = jQuery.parseJSON(ret);
                        led_ebl = data['enable'];
                        $("#led-status").text(led_ebl ? "ON" : "OFF");
                    } else {
                        alert("set led-open failed!");
                    }
                }});
        }
    });
    $("#led-close").click(function() {
        $.ajax({
            type: "POST",
            url: php_exec,
            data: {control:"led-close"},
            success: function(ret) {
                if (ret == 0) {
                    led_ebl = 0;
                    $("#led-status").text("OFF");
                } else {
                    alert("set led-stop failed!");
                }
            }});
    });
    $("#uln2003-start").click(function() {
        if (uln2003_ebl == 1) {
            console.log("already started!");
        } else {
            $.ajax({
                type: "POST",
                url: php_exec,
                async: false,
                data: {control:"uln2003-start"},
                success: function(ret) {
                    if (ret != 1) {
                        var data = jQuery.parseJSON(ret);
                        uln2003_ebl = data['enable'];
                        uln2003_dir = data['direction'];
                        uln2003_spd = data['speed'];
                        $("#uln2003-status").text(uln2003_ebl ? "ON" : "OFF");
                        $("#uln2003-direction").text(uln2003_dir ? "CCW" : "CW");
                        $("#uln2003-speed").text(uln2003_spd);
                    } else {
                        alert("set uln2003-start failed!");
                    }
                }});
        }
    });
    $("#uln2003-stop").click(function() {
        $.ajax({
            type: "POST",
            url: php_exec,
            data: {control:"uln2003-stop"},
            success: function(ret) {
                if (ret == 0) {
                    uln2003_ebl = 0;
                    $("#uln2003-status").text("OFF");
                } else {
                    alert("set uln2003-stop failed!");
                }
            }});
    });
    $("#uln2003-turn").click(function() {
        $.ajax({
            type: "POST",
            url: php_exec,
            data: {control:"uln2003-turn", direction:(uln2003_dir ? 0 : 1)},
            success: function(ret) {
                if (ret == 0) {
                    uln2003_dir = uln2003_dir ? 0 : 1;
                    $("#uln2003-direction").text(uln2003_dir ? "CCW" : "CW");
                } else {
                    alert("set uln2003-turn failed!");
                }
            }});
    });
    $("#uln2003-speedup").click(function() {
        if (uln2003_spd < 5) {
            $.ajax({
                type: "POST",
                url: php_exec,
                data: {control:"uln2003-speed", speed:(uln2003_spd + 1)},
                success: function(ret) {
                    if (ret == 0) {
                        uln2003_spd++;
                        $("#uln2003-speed").text(uln2003_spd);
                    } else {
                        alert("set uln2003-speedup failed!");
                    }
                }});
        } else {
            console.log("the highest speed is 5");
        }
    });
    $("#uln2003-speeddown").click(function() {
        if (uln2003_spd > 1) {
            $.ajax({
                type: "POST",
                url: php_exec,
                data: {control:"uln2003-speed", speed:(uln2003_spd - 1)},
                success: function(ret) {
                    if (ret == 0) {
                        uln2003_spd--;
                        $("#uln2003-speed").text(uln2003_spd);
                    } else {
                        alert("set uln2003-speeddown failed!");
                    }
                }});
        } else {
            console.log("the lowest speed is 1");
        }
    });
});
