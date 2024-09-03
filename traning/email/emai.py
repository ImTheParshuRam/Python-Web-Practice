import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#step1: set up the emial details
sender_email = "parshu13.raam@gmail.com"
reciever_email = "manvi.garg2308@gmail.com"
password = "Parshu13.raam@#_"
subject ="Test Email"
body = " this is a test email sent from python hellooo"

#step 2: create the email content 
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject

#attach the body with the msg instance
message.attach(MIMEText(body, "plain"))

#step 3  set up the smtp server
stmp_server = "smtp.gmail.com"
port =587

try:
    server = smtplib.SMTP(stmp_server, port)
    server.starttls()

    #login to the email account
    server.login(sender_email,password)

    #send the email
    server.sendmail(sender_email, reciever_email,message.as_string())
    print("email sent successfully")

except Exception as e:
    print(f"Error: (e)")
    
finally:
    server.quit() #close the communication