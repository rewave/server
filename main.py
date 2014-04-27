#!/usr/bin/python

import time
from bluetooth import *
from logbook import Logger
from pattern import Pattern
from pykeyboard import PyKeyboard

log = Logger('main.py', level=0)

k = PyKeyboard()

test_case = Pattern(stream=True) #stream of incoming data
templates = [Pattern(template_name="left_wave", key_code=k.left_key)]#, Pattern("right_wave", "Right"), Pattern("flick_up", "Up")]



server_sock=BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "a1a738e0-c3b3-11e3-9c1a-0800200c9a66"

advertise_service(server_sock, "RewaveServer",
				   service_id = uuid,
				   service_classes = [ uuid, SERIAL_PORT_CLASS ],
				   profiles = [ SERIAL_PORT_PROFILE ],  
				)

def match(test_case, template):
	return True


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
			test_case.put(data.split(","))
			
			for template in templates:
				if match(test_case, template):
					k.tap_key(template.key_code)
			
			if data == "quit":
				break
			time.sleep(0.0006)
	except IOError:
		pass
	
	print("disconnected")
	
	client_sock.close()
	print("all done")

server_sock.close()