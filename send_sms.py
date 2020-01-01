#creating Python texting app, using Twilio API
from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)
my_msg = 'This is my message, called my_msg, from send_sms.py'
message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)