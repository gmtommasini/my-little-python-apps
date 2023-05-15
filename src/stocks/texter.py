from twilio.rest import Client
from config import  TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(body):
    message = client.messages.create(
        body = body,
        from_='+12705179282',
        to='+14162701529'
    )
    print(message.sid)
    print(message.status)
    print("Messge sent")