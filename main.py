#! /usr/bin/python3

from bluetooth import BluetoothSocket, RFCOMM, PORT_ANY, SERIAL_PORT_CLASS, SERIAL_PORT_PROFILE

config = {
    'backlog': 5,  # max unsuccesful connect attempts
    'uuid': 'a1a738e0-c3b3-11e3-9c1a-0800200c9a66'
}


class BtServer(object):

    def __init__(self):
        super(BtServer, self).__init__()

        socket = BluetoothSocket(RFCOMM)
        socket.bind(PORT_ANY)
        socket.listen(config['backlog'])

        bound_port = socket.getsockname()[1]
        uuid = config['uuid']

        advertise_service(
            socket,
            "Rewave Server",
            service_id=uuid,
            service_classes=[uuid, SERIAL_PORT_CLASS],
            profiles=[SERIAL_PORT_PROFILE]
        )

        self.socket = server_sock
        self.port = bound_port

        self.client = {}

    def close_connection(self):
        self.client['socket'].close()

    def kill(self):
        self.socket.close()


def main():

    S = BtServer()

    print('Waiting for connection on RFCOMM channel %d' % S.port)
    s.client['socket'], s.client['info'] = S.socket.accept()
    print("Accepted connection from ", s.client['info'])

    while True:
        try:
            data = s.client['socket'].recv(2048).decode(encoding='UTF-8')
            log.debug(data)
            if data == "quit":
                S.close_connection()
                break

            print(data)
            time.sleep(0.0006)
        
        except IOError:
            pass

    S.kill()

if __name__ == '__main__':
    main()
