import os, sys, random
import pandas, json
from datetime import datetime 
from email_sender import send_email

# Utils
def file_path(rel_path):
  return os.path.join(sys.path[0], rel_path)

bds = pandas.read_csv(file_path("birthdays.csv"))

today = datetime.now()
today = today.month, today.day

bd_dict = {(data_row.month, data_row["day"]): data_row for (index, data_row) in bds.iterrows() if (data_row.month, data_row["day"])==today}
print(len(bd_dict))

# for person in bd_dict if (person.name
if today in bd_dict:
  print("IN")
  person = bd_dict[today]
  # print(person)
  with open(file_path(f"letter_templates\\letter_{random.randint(1,3)}.txt")) as letter:
    content = letter.read()
    content = content.replace("[NAME]", person["name"])
  # print(content)

  send_email(to=person.email, subject="Happy Birthday!", body=content)

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



