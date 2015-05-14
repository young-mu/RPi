$(document).ready(function() {
    $("#dht11-hum").click(function() {
        $.ajax({
            type: "POST",
            url: "/sensors.php",
            data: {sensor:"dht11-hum"},
            success: function(hum) {
                if (hum != 0) {
                    $("#dht11-hum").text(hum);
                } else {
                    alert("get dht11-hum failed!");
                }
            }});
    });
    $("#dht11-temp").click(function() {
        $.ajax({
            type: "POST",
            url: "/sensors.php",
            data: {sensor:"dht11-temp"},
            success: function(temp) {
                if (temp !=0) {
                    $("#dht11-temp").text(temp);
                } else {
                    alert("get dht11-temp failed!");
                }
            }});
    });
});