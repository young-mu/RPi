var php_exec = "/php/camera.php";
var reret;
var opt_resolution, width, height;
var opt_quality;
var opt_flip;
var opt_encode;
var opt_delay, delay;
var cd_worker;

function refreshStatus() {
    $.ajax({
        type: "POST",
        url: php_exec,
        async: false,
        data: {camera:"status"},
        success: function(ret) {
            alert(ret);
//            if (ret == 1) {
//                $("#camera-status").text("YES");
//                $("#camera-capture").attr("disabled", false);
//            } else {
//                console.log("camera not available");
//            }
        }});
}

$(document).ready(function() {
    $("#camera-capture").attr("disabled", false);
    refreshStatus();
    $("#camera-refresh").click(refreshStatus);
    $("#camera-capture").click(function() {
        opt_resolution = $("#camera-resolution").val();
        reret = opt_resolution.match(/^-w\ (\d{3,4})\ -h\ (\d{3,4})$/);
        width = reret[1];
        height = reret[2];
        opt_quality = $("#camera-quality").val();
        opt_flip = $("#camera-flip").val();
        opt_encode = $("#camera-encode").val();
        opt_delay = $("#camera-delay").val();
        reret = opt_delay.match(/^-t\ (\d{4,5})$/);
        delay = reret[1] / 1000;

        console.log("opt_resolution: " + opt_resolution);
        console.log("width: " + width + ", height: " + height);
        console.log("opt_quality: " + opt_quality);
        console.log("opt_flip: " + opt_flip);
        console.log("opt_encode: " + opt_encode);
        console.log("opt_delay: " + opt_delay);
        console.log("delay: " + delay);

        $("#camera-countdown").text(delay);
        $("#camera-image").attr("width", width);
        $("#camera-image").attr("height", height);

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
            async: false,
            data: {camera: "capture",
                   resolution: opt_resolution,
                   quality: opt_quality,
                   encode: opt_encode,
                   flip: opt_flip,
                   delay: opt_delay},
            success: function(ret) {
                if (ret != 1) {

                } else {

                }
            }});
    });
});
