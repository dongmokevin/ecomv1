
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC114975f6aab9e371ddb27fad76319556'
auth_token = 'fc5be11292421cfd94d0d7ac43ce7dc5'
client = Client(account_sid, auth_token)

def send_whatsapp_message(body, to):
    message = client.messages.create(
                                  body=body,
                                  from_='whatsapp:+14155238886',
                                  to=f'whatsapp:{to}'
                              )

    print(message.sid)
