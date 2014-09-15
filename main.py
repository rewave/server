#! /usr/bin/python3

from bluetooth import BluetoothSocket, RFCOMM, PORT_ANY, SERIAL_PORT_CLASS, SERIAL_PORT_PROFILE, advertise_service
from pykeyboard import PyKeyboard
from time import sleep

config = {
    'backlog': 5,  # max unsuccesful connect attempts
    'uuid': 'a1a738e0-c3b3-11e3-9c1a-0800200c9a66'
}

k = PyKeyboard()


class BtServer(object):

    def __init__(self):
        super(BtServer, self).__init__()

        self.socket = BluetoothSocket(RFCOMM)
        self.client = {}

    def start(self):
        # empty host address means this machine
        self.socket.bind(("", PORT_ANY))
        self.socket.listen(config['backlog'])

        self.port = self.socket.getsockname()[1]
        uuid = config['uuid']

        advertise_service(
            self.socket,
            "Rewave Server",
            service_id=uuid,
            service_classes=[uuid, SERIAL_PORT_CLASS],
            profiles=[SERIAL_PORT_PROFILE]
        )

        print('Waiting for connection on RFCOMM channel %d' % self.port)
        self.client['socket'], self.client['info'] = self.socket.accept()
        print("Accepted connection from ", self.client['info'])

    def kill(self):
        self.socket.close()

    def close_connection(self):
        self.client['socket'].close()


def main():

    S = BtServer()
    S.start()


    while True:
        try:
            data = S.client['socket'].recv(2048).decode(encoding='UTF-8')

            if data == "exit":
                S.close_connection()
                break

            if len(data) > 0:
                try:
                    k.tap_key(k.lookup_character_keycode(data))
                except KeyError:
                    pass

            print(data)
            sleep(0.0006)

        except IOError:
            pass

        except KeyboardInterrupt:
            break

    S.kill()

if __name__ == '__main__':
    main()
