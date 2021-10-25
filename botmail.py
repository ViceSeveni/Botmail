import smtplib
import os
import codify
# --Codify is one of my own scripts found at https://github.com/ViceSeveni/Codify



def getpassword():
# --include path to file with encrypted password and input it into getpassword()
    passfile = open(r"", 'rb')
    password = passfile.read()
    dec_password = codify.decrypt(password)
    return dec_password

def botmail(subject='', message=''):
# --Enter your bots email address here
    botname = ''
# --Enter the recipients email here. Turn into an input function as needed.
# --I mainly used this to send myself text information quickly.
    recipient = ''
    password = getpassword()
    os.system('cls')

    if subject == '':
        subject = input('Subject: ')
    if message == '':
        message = input('Message: ')
# --This is my own personal addition. Encrypts your message for security.
#         message = codify.encrypt(message)

# --Gmail is common, but doesn't mean you use it. Change this as needed.
    conn = smtplib.SMTP('smtp.gmail.com', '587')

    conn.ehlo()
    conn.starttls()
    conn.login(botname,password)
    conn.sendmail(botname, recipient, f'Subject: {subject}\n\n{message}')
    conn.quit()

if __name__ == '__main__':
    botmail()
