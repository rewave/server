#!/usr/bin/python


import time, csv

from bluetooth import *
from pykeyboard import PyKeyboard
from logbook import Logger

log = Logger('main.py', level=0)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]


#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
uuid = "a1a738e0-c3b3-11e3-9c1a-0800200c9a66"

advertise_service( server_sock, "RewaveServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

test_case = []
max_template_length = 40


def get_max_template_length():
    pass

while True:
    print("Waiting for connection on RFCOMM channel %d" % port)
    
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    
    try:
        while True:
            data = client_sock.recv(2048).decode(encoding='UTF-8')
            log.debug(data)
            
            if (len(test_case) > 40):
                del(test_case[0])
            test_case.append(data.split(","))
            


            if data == "quit":
                break
            time.sleep(0.0006)
    except IOError:
        pass
    
    print("disconnected")
    
    client_sock.close()
    print("all done")
server_sock.close()
