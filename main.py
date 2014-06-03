#!/usr/bin/python

import time
from bluetooth import *
from logbook import Logger
from pykeyboard import PyKeyboard

log = Logger('main.py', level=0)

k = PyKeyboard()



def create_server():
	server_socket=BluetoothSocket(RFCOMM)
	server_socket.bind(("",PORT_ANY))
	server_socket.listen(1)

	port = server_socket.getsockname()[1]

	uuid = "a1a738e0-c3b3-11e3-9c1a-0800200c9a66"

	advertise_service(server_socket, "RewaveServer",
						service_id = uuid,
						service_classes = [ uuid, SERIAL_PORT_CLASS ],
						profiles = [ SERIAL_PORT_PROFILE ]
					)
	return server_socket, port


server_sock, port = create_server()

while True:
	print("Waiting for connection on RFCOMM channel %d" % port)
	
	try:
		client_sock, client_info = server_sock.accept()
		print("Accepted connection from ", client_info)
	
	except KeyboardInterrupt:
		break

	try:
		while True:
			data = client_sock.recv(2048).decode(encoding='UTF-8')
			log.debug(data)
			if data == "quit":
				break
			if data == "is_server_present":
				client_sock.send(1).encode(encoding='UTF-8')

			time.sleep(0.0006)
	except IOError:
		pass
	
	print("disconnected")
	
	client_sock.close()
	print("all done")

server_sock.close()