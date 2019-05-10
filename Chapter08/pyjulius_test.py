#!/usr/bin/env python
import sys

#Importing pujulius module
import pyjulius

#It an implementation of FIFO(First In First Out) queue suitable for multi threaded programming.
import Queue

# Initialize Julius Client object with localhost ip and default port of 10500 and trying to connect server.
client = pyjulius.Client('localhost', 10500 )
try:
    client.connect()
#When the client run before executing the server it will make a connection error.
except pyjulius.ConnectionError:
    print 'Start julius as module first!' 
    sys.exit(1)


# Start listening to the server
client.start()
try:
    while 1:
        try:
            	#Fetching recognition result from server
			result = client.results.get(False)
        except Queue.Empty:
            continue
        print result  
except KeyboardInterrupt:
    print 'Exiting...'
    client.stop()  # send the stop signal
    client.join()  # wait for the thread to die
    client.disconnect()  # disconnect from julius 
