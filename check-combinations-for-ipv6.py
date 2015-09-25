#!/usr/bin/env python

import fileinput
import socket
import ssl

def hasipv6(host):
	
    try:
        info = socket.getaddrinfo(host, 80, socket.AF_INET6, socket.SOCK_STREAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
    except:
        return
    ipv6=info[0][4][0]

    try:
	    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	    s.settimeout(2)
	    s.connect((ipv6, 119))
	    s.close()
	    print host, "has IPv6", ipv6, "with succesful connect on port 119"
    except:
	#print host, "has IPv6", ipv6, "but no connect on port 119"
	try:
		    # WRAP SOCKET
		    wrappedSocket = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
		    # CONNECT
		    wrappedSocket.connect((ip, 563))
		    # CLOSE SOCKET CONNECTION
		    wrappedSocket.close()
		    print host, "has IPv6", ipv6, "with succesful connect on port 563"
	except:
		print host, "has IPv6", ipv6, "with no connect on port 119 nor 563"
		

for line in fileinput.input():
	domain=line.rstrip()
	hasipv6("reader." + domain)
	hasipv6("news." + domain)
	hasipv6("block." + domain)
	hasipv6("eu." + domain)
	hasipv6("us." + domain)

	pass


