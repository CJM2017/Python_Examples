#!/usr/bin/python

import socket
import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


# Message pipeline
s = socket.socket() # create the socket
host = socket.gethostname() # get local machine name
port = 3000 # use this port for services
s.bind((host,port)) # bind to the port
s.listen(5)	# wait for a client connection
connection, addr = s.accept()

app = Flask(__name__)

# Remove the server logging 
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Handle server routing
@app.route('/sms', methods = ['POST'])
def sms():
	# Obtain info from requestor
	number = request.form['From']
	body = request.form['Body']

	# Creat the display message
	dispMessage = '\n[Char]: {}'.format(body)

	# Display to terminal
	connection.send(dispMessage)

	# Return null response 
	resp = MessagingResponse()
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=False)
	connection.close()


"""
	want to create a pipe so that this process sends information 
	from the webhook incoming sms message to the outgoing application 
	which handles the sending of the users messages and the display
	of the entire conversation
"""