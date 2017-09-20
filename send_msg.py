
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2afcb42f8dfbcd68a1185fb0d0fbb27f"
# Your Auth Token from twilio.com/console
auth_token  = "4aeb772390973a22944d42813b6b6845"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18297639602", 
    from_="+14438326746",
    body="KLK menol")

print(message.sid)