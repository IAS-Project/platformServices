from twilio.rest import Client

def send_whatsapp_notification(to_number, message, account_sid, auth_token):
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to_number}'
    )

    print(f"WhatsApp notification sent to {to_number}, Message SID: {message.sid}")

to_number = '+917021794108'
message = "Hello, this is a notification message!"

account_sid = "ACef0a0280e62b5f9afeb8707d73b3053d"
auth_token = "66ec1a3be77bfc9446a246839b4f7ac0"

send_whatsapp_notification(to_number, message, account_sid, auth_token)


psw = 'pkjvtsmvofuqpjaz'
emails = [
    {
        "email": "gandhisanya99@gmail.com",
        "Sub": "Fail system",
        "Body": {
            "name": "Load Balancer",
            "Containerid": "122",
            "VMhost": "1212"
        },
        "status": "killed"
    },
    {
        "email": "yashsampat23154@gmail.com",
        "Sub": "Warning",
        "Body": {
            "name": "Web Server",
            "Containerid": "234",
            "VMhost": "5678"
        },
        "status": "exceeded"
    }
]

import smtplib
def send_mail(sender_email , receiver_email,password,sub, body):
    message = f"Subject: {sub} \n\n{body}"
    # message += f"Name of subsystem is {body['name']}\n"
    # message += f"Container id  is {body['Containerid']}\n"
    # message += f"VMhost  is {body['VMhost']}\n\n"
    # message += 'This is a testing message now it worked,\n tell the changes and the format' 
    #create connection
    server = smtplib.SMTP('smtp.gmail.com')
    #start TLS
    server.starttls()
    print('Connectin made successfully')

    server.login(sender_email, password)
    print('Login successful to server')
    # Send the email
    server.sendmail(sender_email, receiver_email, message)
    print(f'message send successfully to {receiver_email}')

    server.quit()
    
for email in emails:
    sender_email = "sharmameritnation@gmail.com"
    receiver_email = email["email"]
    password = psw
    subject = email["Sub"]
    body = f"Name: {email['Body']['name']}\nContainer ID: {email['Body']['Containerid']}\nVM Host: {email['Body']['VMhost']}\nStatus: {email['status']}"
    send_mail(sender_email, receiver_email, password, subject, body)
    # print(body)