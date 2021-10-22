# Client Class

import socket
import threading
import os
import sys
import select
from time import sleep

class Transmit(threading.Thread):
  def run(self):
		# Sending data to the server
	    print('Transmit started')

	    global s
        # connection
	    global threadRunning
	    while(threadRunning):
			# Read text with 1 sec timeout
		    i, o, e = select.select( [sys.stdin], [], [], 1 )
		    if(i):
			    string = sys.stdin.readline().strip() + '\r\n'
			    byteArray = bytearray(string, "utf-8") # Convert string into a b$
			    s.sendall(byteArray)

		#print('Transmit stopped - threadRunning')
	    return

class Receive(threading.Thread):
	def run(self):
		# Receiving data from the server
		#print('Receive started')
		global s 
        # connection
		global threadRunning
		while(threadRunning):
			# Use 1 second timeout on receive
			ready = select.select( [s], [], [], 1 )
			if(ready[0]):
				data = s.recv(1024).strip()
				if(len(data) == 0): # Connection closed by server
					threadRunning = False
				else:
					print('Received:', data.decode("utf-8")) # Converts the receive$

			sleep(0.1)

		#print('Receive stopped - threadRunning')
		return

# Running main program
HOST = '00.0.0.00' # The remote host IP
PORT = 0000 # The same port as used by the server 
global threadRunning # Used to stop threads
threadRunning = False
global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

os.system('clear')
print('Connection with server established')

try:
	print("----------------------------------")
	print("        M A I N - M E N U")
	print(' Press CTRL+C to close connection')
	print("---------------------------------")
	# Create instance of class
	threadRunning = True
	transmit = Transmit()
	receive = Receive()
	# Start class
	transmit.start()
	receive.start()
	while(threadRunning):
		sleep(0.1)

except KeyboardInterrupt: 
    # Stop program when CTRL+C is pressed
	
	threadRunning = False
	sleep(2)
	s.close()

finally:
	s.close()