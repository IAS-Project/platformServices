#for whatsapp services 
# !pip install twilio
# from twilio.rest import Client
# !pip install smtplib
import smtplib
#for email services
#email of sender and password 
#its a random generated password from google account
#it has to be done manually
sender_email = "sharmameritnation@gmail.com"
sender_psw = 'pkjvtsmvofuqpjaz'
#------------till now manual otherwise a function for
#------------taking arguments is required
'''
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
'''
#------------------send message completed---------------------
#------------------send emails started ------------------------

emails = [
    {
        "email": "gandhisanya99@gmail.com",
        "Sub": "sorry guys ignore maro",
        "Body": {
            "name": "Load Balancer",
            "Containerid": "122",
            "VMhost": "1212"
        },
        "status": "killed"
    },
    {
        "email": "yashsampat23154@gmail.com",
        "Sub": "sorry guys ignore maro",
        "Body": {
            "name": "Web Server",
            "Containerid": "234",
            "VMhost": "5678"
        },
        "status": "exceeded"
    }
]


def send_mail(sender_email , receiver_email,password,sub, body):
    message = f"Subject: {sub} \n\n{body}"
    '''# message += f"Name of subsystem is {body['name']}\n"
    # message += f"Container id  is {body['Containerid']}\n"
    # message += f"VMhost  is {body['VMhost']}\n\n"
    # message += 'This is a testing message now it worked,\n tell the changes and the format' 
    #create connection'''
    try:
        server = smtplib.SMTP('smtp.gmail.com')
        #start TLS
        server.starttls()
        # print('Connectin made successfully')

        try:
            server.login(sender_email, password)
            # print('Login successful to server')
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Failed to login. Please check your credentials and try again.")
            return
            
        try:
            # Send the email
            result = server.sendmail(sender_email, receiver_email, message)
            if not result:
                print(f'message send successfully to {receiver_email}')
            else:
                print(f'Failed to send email to {result.keys()}')

        except Exception as e:
            print(f"Error: {str(e)}")
            print("Failed to send email. Please check the email addresses provided and try again.")
            return
        finally:
            #close the connection
            server.quit()
    except Exception as e:
        print(f"Error {str(e)}")
        print("Failed to connect to Smtp. Please check internet connectivity")
    
for email in emails:
    sender_email = sender_email
    password = sender_psw
    receiver_email = email["email"]
    subject = email["Sub"]
    body = f"Name: {email['Body']['name']}\nContainer ID: {email['Body']['Containerid']}\nVM Host: {email['Body']['VMhost']}\nStatus: {email['status']}"
    send_mail(sender_email, receiver_email, password, subject, body)
    # print(body)
