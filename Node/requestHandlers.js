var exec = require("child_process").exec;

function start(response) {
    console.log("request handler 'start' was called");
    exec("ls -lah /srv/http", function(error, stdout, stderr) {
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.write(stdout);
        response.end();
    });
}

exports.start = start;
