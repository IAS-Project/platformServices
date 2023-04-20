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

def send(sender_email , receiver_email, password, sub = "", body = ""):
    #sender_email : email of sender
    #receiver_email : email of receiver
    #password prefer this link to generate  https://support.google.com/mail/answer/185833?hl=en
    message = f"Subject: {sub} \n\n{body}"
    try:
        server = smtplib.SMTP('smtp.gmail.com')
        #start TLS
        server.starttls()
        try:
            server.login(sender_email, password)
            # print('Login successful to server')
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Failed to login. Please check your credentials and try again.")
            print("Generate less secure key, Check it out https://support.google.com/mail/answer/185833?hl=en")
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
        
def send_mail(sender_email , receiver_email, password, sub = "Welcome buddies", body = "Thanks for using our platform, please check the code,\n updated in github"):
    #Broadcasting message to all if it is a list
    if isinstance(receiver_email, list):
        for receiver in receiver_email:
            # Send email to each receiver
            send(sender_email , receiver, password, sub, body)
    else:
        # Send email to single receiver
        send(sender_email , receiver_email, password, sub, body)
         
    
# x = ["gandhisanya99@gmail.com", "lokeshsharma123456@gmail.com","yashsampat23154@gmail.com"]
# y = "lokeshsharma123456@gmail.com"
send_mail(sender_email, x, sender_psw)

 