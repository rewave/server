var net = require('net');
var fs = require('fs');

var HOST = '127.0.0.1';
var PORT = 3000;
var timeout = 420000; // msec

var lg = function (message) {
	console.log(message);
};

var server = net.createServer();

server.on('listening', function () {
	lg('Server listening on ' + HOST + ':' + PORT);
});

server.on('connection', function (sock) {
	console.log("connection");
	sock.setTimeout(timeout, function () {
		try {
			sock.end();
		} catch (x) {
			lg('on end' + x);
		}
	});

	sock.setNoDelay(true);

	sock.setEncoding('ascii');

	sock.on('data', function (data) {
		try {
			sock.write(data);
		} catch (x) {
			lg(x);
		}
	});

	sock.on('end', function (data) {
		try {
			sock.end();
		} catch (x) {
			lg('on end' + x);
		}
	});

	sock.on('error', function (err) {
		lg(err);
	});

	sock.on('close', function (data) {

		try {
			sock.end();
		} catch (x) {
			lg(x);
		}

		try {
			sock.destroy();
		} catch (x) {
			lg('on close' + x);
		}
	});

	sock.on('timeout', function () {});
});

server.on('error', function (err) {});

server.on('close', function () {});

server.listen(PORT, HOST);