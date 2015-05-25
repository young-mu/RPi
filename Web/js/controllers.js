$(document).ready(function() {
    $("#uln2003-start").click(function() {
        $.ajax({
            type: "POST",
            url: "/controllers.php",
            data: {control:"uln2003-start"},
            success: function(ret) {
                if (ret != 0) {
                    alert("set uln2003-start failed!");
                }
            }});
    });
    $("#uln2003-stop").click(function() {
        $.ajax({
            type: "POST",
            url: "/controllers.php",
            data: {control:"uln2003-stop"},
            success: function(ret) {
                if (ret != 0) {
                    alert("set uln2003-stop failed!");
                }
            }});
    });
    $("#uln2003-speedup").click(function() {
        $.ajax({
            type: "POST",
            url: "/controllers.php",
            data: {control:"uln2003-speedup"},
            success: function(ret) {
                if (ret != 0) {
                    alert("set uln2003-speedup failed!");
                }
            }});
    });
    $("#uln2003-speeddown").click(function() {
        $.ajax({
            type: "POST",
            url: "/controllers.php",
            data: {control:"uln2003-speeddown"},
            success: function(ret) {
                if (ret != 0) {
                    alert("set uln2003-speeddown failed!");
                }
            }});
    });
});
