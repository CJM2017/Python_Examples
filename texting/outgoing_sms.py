#!/usr/bin/python
# 
# Author	: Connor McCann	
# Product	: SMS Chat
# Date		: 13 Jun 2017
#
# Installs
#			: pip install twilio
#			: pip install flask
#
import sys
import json
import socket
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect


def main():
	# Client connections
	s = socket.socket()
	host = socket.gethostname()
	port = 3000

	# People to talk to
	contacts = {'char':'16313745510',
				'connor':'15083675434'}
	okToSend = True

	# Twilio connection 
	configFilePath = "../../twilio_account/config.json"
	with open(configFilePath) as jsonFile:
		account = json.load(jsonFile)
	client = Client(account['setup']['accountSid'], account['setup']['authToken'])

	# Message details
	recipient = sys.argv[1]
	number = contacts[recipient]

	s.connect((host,port)) # blocking
	while (True):
		print(s.recv(1024)) # blocking
		msgString = raw_input('[Connor]: ') # blocking
		if (okToSend):
			message = client.api.account.messages.create(to=number,
													 from_="16179967175", # Somerville Area Code
													 body=msgString)
	s.close()
	return

if __name__ == "__main__":
	sys.exit(main())