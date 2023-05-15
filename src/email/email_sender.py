import smtplib
import os



my_email="guitommasini+sender@gmail.com"
password = os.environ.get("GMAIL_PASSWORD")
dest_email = "guitommasini+dest@gmail.com"

def send_email(to=dest_email, subject="Email Subject" , body="This is the body"):
  with  smtplib.SMTP("smtp.gmail.com") as connection:
    # Starting Transport Layer Security
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr=my_email, 
      to_addrs=dest_email, 
      msg=f"Subject:{subject}\n\n{body}"
      )
