import smtplib
import ssl
import csv
from email.message import EmailMessage


# اطلاعات اتصال به سرور ایمیل را نگه می‌دارم.
class SmtpConfig:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port


# ایمیل را می‌سازم و از طریق SMTP می‌فرستم.
def send_email(config, recipient_email, text_body, html_body):
    message = EmailMessage()
    message["Subject"] = "A message for you"
    message["From"] = config.sender_email
    message["To"] = recipient_email

    message.set_content(text_body)
    message.add_alternative(html_body, subtype="html")

    try:
        with smtplib.SMTP(config.smtp_server, config.smtp_port, timeout=20) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(config.sender_email, config.sender_password)
            server.send_message(message)
    except (smtplib.SMTPException, OSError) as error:
        raise RuntimeError(str(error)) from error


# لیست گیرنده‌ها را از فایل CSV می‌خوانم.
def read_recipients(file_path):
    recipients = []

    with open(file_path, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if not reader.fieldnames or "name" not in reader.fieldnames or "email" not in reader.fieldnames:
            raise ValueError("CSV must contain 'name' and 'email' columns.")

        for row in reader:
            name = row.get("name", "").strip()
            email = row.get("email", "").strip()

            if name and email:
                recipients.append({"name": name, "email": email})

    return recipients


# متن فایل قالب ایمیل را می‌خوانم.
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as text_file:
        return text_file.read()
