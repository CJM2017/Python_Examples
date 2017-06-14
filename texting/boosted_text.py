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
import os
import json
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect


contacts = {'char':'16313745510'}
okToSend = False

def buildString(words):
	message = ''
	for word in words:
		message += word
		message += " "
	return message

def main():
	# Twilio connection 
	configFilePath = "../../twilio_account/config.json"
	with open(configFilePath) as jsonFile:
		account = json.load(jsonFile)
	client = Client(account['setup']['accountSid'], account['setup']['authToken'])

	# Message details
	recipient = sys.argv[1]
	number = contacts[recipient]
	msgString = ''
	words = sys.argv[2:]
	numWords = len(words)

	# Build the string
	if (numWords >= 1):
		msgString = buildString(words)
		print(number)
		print(msgString)

	if (okToSend):
		message = client.api.account.messages.create(to=number,
												 from_="16179967175", # Somerville Area Code
												 body=msgString)

	return

if __name__ == "__main__":
	sys.exit(main())