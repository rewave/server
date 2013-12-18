#!\usr\bin\python

"""
Stream Server
"""

import socket
import sys

host = None      # Symbolic name meaning all available interfaces
port = 50007     # Arbitrary non-privileged port

#socket.getaddrinfo(host, port, family, socktype, proto, flags)
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE):
	print res
	af, socktype, proto, canonname, sa = res
	try:
		#get socket file descriptor
		s = socket.socket(af, socktype, proto)
	except socket.error as msg:
		print msg
		s = None
		continue

	try:
		#bind socket
		s.bind(sa)
		s.listen(1)
	except socket.error as msg:
		print msg
		s.close()
		s = None
		continue
	break

if s is None:
	print 'could not open socket'
	sys.exit(1)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
	data = conn.recv(1024)
	print data
conn.close()