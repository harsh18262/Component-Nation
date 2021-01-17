sender_email = "componentnation@gmail.com"  # Enter your address
password = ''

def send_mail(receiver_email,html):
  import requests
  import smtplib, ssl

  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText

  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"

  # Create message container - the correct MIME type is multipart/alternative.
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Thank You For Using Component Nation"
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # Create the body of the message (a plain-text and an HTML version).
  text = " "

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')


  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.
  msg.attach(part1)
  msg.attach(part2)



  # Send the message via local SMTP server.

  # sendmail function takes 3 arguments: sender's address, recipient's address
  # and message to send - here it is sent as one string.

  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email,  msg.as_string())


#overloaded to work for callback form
def callback_mail(receiver_email,email,Name,sub,body):
  import requests
  import smtplib, ssl

  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText

  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Request"
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # Create the body of the message (a plain-text and an HTML version).
  text = "Name: "+Name+"\nEmail: "+email+"\nSubject:"+sub+"\nMessage:\n"+body+"\n"

  part1 = MIMEText(text, 'plain')


  msg.attach(part1)


  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email,  msg.as_string())
