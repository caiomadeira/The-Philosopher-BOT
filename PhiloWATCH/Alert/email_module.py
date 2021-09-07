import smtplib
import os
from PhiloWATCH.Logs_pw.logger import log
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_alert(use_subject):
    load_dotenv()

    sender_email = os.getenv('sender_email')
    receiver_email = os.getenv('receiver_email')
    password = os.getenv('sender_email_pwd')

    message = MIMEMultipart("alternative")
    message["Subject"] = use_subject
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    ATENÇÃO!"""

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    try:
        with smtplib.SMTP(host="outlook.office365.com", port=587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        log.error("[+] - E-mail de alerta enviado com sucesso!")

    except Exception as send_email_error:
        log.error("[X] - Falha no envio de e-mail.")
        log.error(send_email_error)
