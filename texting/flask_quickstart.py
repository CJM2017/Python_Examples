#!/usr/bin/python

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/sms', methods = ['POST'])
def sms():
	number = request.form['From']
	body = request.form['Body']
	print(body)

	resp = MessagingResponse()
	resp.message('message received')
	return str(resp)
	
if __name__ == "__main__":
	app.run(debug=True)