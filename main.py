# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC8957a43d3dfe61ff402c03cdb7904fe1"
auth_token = "Your Auth Token Here"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Testing my python skills #Pen15 ",
  from_="+19704636773",
  to="+Your number here"
)

print(message.sid)
