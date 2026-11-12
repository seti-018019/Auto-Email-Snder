# Auto Mail Sender

A small Python project that reads recipients from a CSV file and sends each person a plain-text and HTML email.

## Requirements

- Python 3.10 or newer
- Access to an SMTP server
- An email account and, if required by the provider, an app password

## Files

- `main.py`: reads the CSV and templates, asks for SMTP details, and sends the emails.
- `mailer.py`: builds and sends the email.
- `recipients.csv`: recipient names and email addresses.
- `templates/email.txt`: plain-text email template.
- `templates/email.html`: HTML email template.

## Setup

1. Open a terminal in this folder.
2. Check your Python version:

   ```bash
   python --version
   ```

3. Edit `recipients.csv` and replace the example addresses with addresses you are allowed to email.
4. Edit the templates if you want to change the message.

No external Python packages are required; the project uses Python's standard library.

## Run

```bash
python main.py
```

The program asks for the sender's email address, email app password, SMTP server, and SMTP port. The password is hidden while typing. For providers that support STARTTLS, port `587` is commonly used, but use the settings supplied by your email provider.

Do not use your normal account password if your provider recommends an app password. Do not share your password or commit it to GitHub.

## Important

Start by testing with your own email address in `recipients.csv`. Sending many unsolicited messages may violate the email provider's rules. This project is intended for learning and for sending messages to recipients who expect them.
