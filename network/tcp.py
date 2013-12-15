#!\usr\bin\python

import SocketServer

class ConnectionHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024)
		print self.data

if __name__== "__main__":
	host, port = "localhost", 9999
	server = SocketServer.TCPServer((host, port), ConnectionHandler)

	try:
		print "TCP server running on %s:%s"%(host, port)
		server.serve_forever()
	except Exception as e:
		print str(e)