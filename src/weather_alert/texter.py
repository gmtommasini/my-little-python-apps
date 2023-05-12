from env import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client


# https://www.twilio.com/docs/sms/quickstart/python 

sent = True

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def text_me(body):  
  if sent:
    print('SMS sent today already')
  else:
    sent = True
    message = client.messages \
                    .create(
                        body=body,
                        from_='+12705179282',
                        to='+14162701529'
                    )

    print(message.sid)
    print(message.status)