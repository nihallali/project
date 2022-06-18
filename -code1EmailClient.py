#!usr/bin/python

# Build input code for customer's email.
# Build attachment for pdf filetype
# Build mail server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = 'Hello from network programming. Have a great day ;)'
sender = 'fazalurrahman2005@gmail.com'
# Get the password in the gmail by: manage your google account >> click on the avatar on the right
# then go to security (right) >> app password (center)
# MUST HAVE 2-FA ENABLED FOR THIS TO WORK!!
# insert the password and then choose mail and this computer and then generate
# copy the password
password = 'xipkeefddpqoqxul'

# put the email of the receiver here
receiver = input("What is the Customer's Email?: ")
# subject here
subject = 'Invoice'
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

pdf_name = input("Drop PDF here: ")

# Open PDF to Binary
binary_pdf = open(pdf_name, 'rb')

payload = MIMEBase('application', 'octet-stream', Name=pdf_name)
payload.set_payload(binary_pdf.read())

# binary to base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdf_name)
message.attach(payload)

# SMTP setup
session = smtplib.SMTP('smtp.gmail.com', 587)

# Security
session.starttls()

# Login
session.login(sender, password)

text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')
