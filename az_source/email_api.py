import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from io import StringIO

# Logging on the INFO level
logging.basicConfig(level=logging.INFO)


SMTP_SERVER = ""
EMAIL_SENDER = ""
EMAIL_SENDER_PASSWORD = ""
EMAIL_RECEIVER = ""
EMAIL_CC_RECEIVER = ""
attachment_name = ""
attachment_data = ""
email_subject = ""
email_body = ""
mail_message = ""


def email_message_only(mail_server: str, 
                 username: str, 
                 password: str, 
                 mail_receiver: str,
                 message: str) -> None:
    with smtplib.SMTP(mail_server, 587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=mail_receiver, msg=message)
    # either "with" or "try/except" block
    # "with" can also throw an exception


def email_with_attachment(email_server: str,
                          username: str,
                          password: str,
                          email_msg_subject: str,
                          email_msg_body: str,
                          email_attach_name: str,
                          email_attach_data: str,
                          email_receiver: str,
                          email_cc_receiver: str = "") -> None:
    # create a message and set headers
    message = MIMEMultipart()
    message["From"] = username
    message["To"] = email_receiver
    message["Subject"] = email_msg_subject
    message["Cc"] = email_cc_receiver
    message.add_header("Content-Type", "text/html")
    # add email body to message, plain or html
    message.attach(MIMEText(email_msg_body, "plain"))
    # attachment
    attachment = StringIO(email_attach_data)
    message.attach(MIMEApplication(attachment.read(), Name=email_attach_name))
    # message to string
    msg_string = message.as_string()
    with smtplib.SMTP(email_server, 587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=([email_receiver] + [email_cc_receiver]), msg=msg_string)
    logging.info("Email sent - successful!")


def main() -> None:
    # email_message_only(SMTP_SERVER, EMAIL_SENDER, EMAIL_SENDER_PASSWORD, EMAIL_RECEIVER, mail_message)
    email_with_attachment(SMTP_SERVER, EMAIL_SENDER, EMAIL_SENDER_PASSWORD, 
                          email_subject, email_body, attachment_name, 
                          attachment_data, EMAIL_RECEIVER, EMAIL_CC_RECEIVER)


if __name__ == "__main__":
    main()
