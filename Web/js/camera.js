var php_exec = "/php/camera.php";
var reret;
var opt_resolution;
var opt_quality;
var opt_flip;
var opt_encode, encode;
var opt_delay, delay;
var cd_worker;

function refreshStatus() {
    $.ajax({
        type: "POST",
        url: php_exec,
        async: false,
        data: {camera:"status"},
        success: function(ret) {
            if (ret == 1) {
                $("#camera-status").text("YES");
                $("#camera-capture").attr("disabled", false);
                console.log("camera is available");
            } else {
                console.log("camera is NOT available");
            }
        }});
}

$(document).ready(function() {
    refreshStatus();
    $("#camera-refresh").click(refreshStatus);
    $("#camera-capture").click(function() {
        $("#camera-image").attr("src", "");
        opt_resolution = $("#camera-resolution").val();
        opt_quality = $("#camera-quality").val();
        opt_flip = $("#camera-flip").val();
        opt_encode = $("#camera-encode").val();
        reret = opt_encode.match(/^-e\ ([a-z]{3})$/);
        encode = reret[1];
        opt_delay = $("#camera-delay").val();
        reret = opt_delay.match(/^-t\ (\d{4,5})$/);
        delay = reret[1] / 1000;

        console.log("opt_resolution: " + opt_resolution);
        console.log("opt_quality: " + opt_quality);
        console.log("opt_flip: " + opt_flip);
        console.log("opt_encode: " + opt_encode);
        console.log("encode: " + encode);
        console.log("opt_delay: " + opt_delay);
        console.log("delay: " + delay);

        $("#camera-countdown").text(delay);

        cd_worker = new Worker("js/camera-countdown.js");
        console.log("start camera-countdown worker");
        cd_worker.onmessage = function(event) {
            dcounter = delay - event.data;
            $("#camera-countdown").text(dcounter);
            if (dcounter == 0) {
                cd_worker.terminate();
                console.log("terminate camera-countdown worker");
                $("#camera-capture").attr("disabled", false);
            }
        }

        $("#camera-capture").attr("disabled", true);

        $.ajax({
            type: "POST",
            url: php_exec,
            async: true,
            data: {camera: "capture",
                   resolution: opt_resolution,
                   quality: opt_quality,
                   encode: opt_encode,
                   flip: opt_flip,
                   delay: opt_delay},
            success: function(ret) {
                if (ret == 0) {
                    console.log("capture successfully");
                    $("#camera-image").attr("src", "image."+encode);
                } else {
                    console.log("capture failed");
                }
            }});
    });
});
