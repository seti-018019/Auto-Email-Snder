import html
from pathlib import Path
from getpass import getpass
from mailer import SmtpConfig, send_email, read_text_file, read_recipients


def main():
    # مسیر فایل‌های پروژه را مشخص می‌کنم.
    project_folder = Path(__file__).parent
    recipients_file = project_folder / "recipients.csv"
    text_template_file = project_folder / "templates" / "email.txt"
    html_template_file = project_folder / "templates" / "email.html"

    try:
        recipients = read_recipients(recipients_file)
        text_template = read_text_file(text_template_file)
        html_template = read_text_file(html_template_file)
    except Exception as error:
        print(f"Could not load project files: {error}")
        return

    if not recipients:
        print("No valid recipients were found in recipients.csv.")
        return

    sender_email = input("Sender email address: ").strip()
    sender_password = getpass("Email app password: ")
    smtp_server = input("SMTP server (for example, smtp.gmail.com): ").strip()
    smtp_port_text = input("SMTP port (usually 587): ").strip()

    try:
        smtp_port = int(smtp_port_text)
    except ValueError:
        print("The SMTP port must be a number.")
        return

    if not 1 <= smtp_port <= 65535:
        print("The SMTP port must be between 1 and 65535.")
        return

    if not sender_email or not sender_password or not smtp_server:
        print("Sender email, app password, and SMTP server are required.")
        return

    smtp_config = SmtpConfig(sender_email, sender_password, smtp_server, smtp_port)

    for recipient in recipients:
        text_body = text_template.format(name=recipient["name"])
        html_body = html_template.format(name=html.escape(recipient["name"]))

        try:
            send_email(
                smtp_config,
                recipient["email"],
                text_body,
                html_body,
            )
            print(f"Email sent to {recipient['name']} ({recipient['email']}).")
        except (RuntimeError, ValueError) as error:
            print(f"Could not send email to {recipient['email']}: {error}")


if __name__ == "__main__":
    main()
