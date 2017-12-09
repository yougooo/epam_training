import smtplib
from email.MIMEText import MIMEText


def mail_from(text, subj, user, destination):
    pass


def send_mail(server, user, passwd, destination, message):
    pass


if __name__ == '__main__':

    user = 'yougooo10@gmail.com'
    destination = 'devops2017dutepam@gmail.com'
    text = 'hello test!\nwith best wishes, Pyvovar Olesksii.'
    subj = 'test email send'
    server = "smtp.gmail.com"
    user_name = "yougooo10@gmail.com"
    msg = MIMEText(text)
    msg["Subject"] = subj
    msg["From"] = user
    msg["To"] = destination
    message = msg.as_string()

    with open('passwd.txt','r') as secret:
        user_passwd = secret.read()

    connect = smtplib.SMTP(server,587)
    connect.ehlo()
    connect.starttls()
    connect.ehlo()
    connect.login(user, user_passwd)
    connect.sendmail(user, destination, message)
    connect.quit()



