import os
from twilio.rest import Client

account_sid = os.environ['Twilio_Account_SID']
auth_token = os.environ['Twilio_Auth_Token']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testing Twilio. Do not Reply",
                     from_='twilio number',
                     to='any valid number'
                 )

print(message.sid)

