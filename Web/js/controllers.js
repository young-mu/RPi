var uln2003_ebl;
var uln2003_dir;
var uln2003_spd;

$(document).ready(function() {
    $("#uln2003-start").click(function() {
        $.ajax({
            type: "POST",
            url: "/php/controllers.php",
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
    });
    $("#uln2003-stop").click(function() {
        $.ajax({
            type: "POST",
            url: "/php/controllers.php",
            data: {control:"uln2003-stop"},
            success: function(ret) {
                alert(ret);
//                if (ret == 0) {
//                    uln2003_ebl = 0;
//                    $("#uln2003-status").text("OFF");
//                } else {
//                    alert("set uln2003-stop failed!");
//                }
            }});
    });
    $("#uln2003-turn").click(function() {
        $.ajax({
            type: "POST",
            url: "/php/controllers.php",
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
                url: "/php/controllers.php",
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
            alert("the highest speed is 5");
        }
    });
    $("#uln2003-speeddown").click(function() {
        if (uln2003_spd > 0) {
            $.ajax({
                type: "POST",
                url: "/php/controllers.php",
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
            alert("the lowest speed is 1");
        }
    });
});
