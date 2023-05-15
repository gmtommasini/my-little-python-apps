import datetime as dt
import os, sys, random
from email_sender import send_email

# Utils
def file_path(rel_path):
  return os.path.join(sys.path[0], rel_path)

now =dt.datetime.now()
weekday= now.weekday()
print(weekday)

if weekday==0:
  with open(file_path("quotes.txt")) as qf:
    quotes = qf.readlines()
    quote = random.choice(quotes)
    
  print(quote)    
  send_email(subject="Today's Motivation", body=quote)
else:
  print("Today is not Monday")