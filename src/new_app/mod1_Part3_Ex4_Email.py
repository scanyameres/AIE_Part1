import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Replace these placeholders with your SMTP server details.
SMTP_HOST = "smtp.example.com"
SMTP_PORT = 2525
SMTP_USERNAME = "YOUR_SMTP_USERNAME"
SMTP_PASSWORD = "YOUR_SMTP_PASSWORD"

SENDER = "sender@example.com"
RECIPIENT = "recipient@example.com"


def send_html_email():
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test HTML email"
    message["From"] = SENDER
    message["To"] = RECIPIENT

    plain_text = "Hello! This is the plain-text version of the email."
    html_text = """
    <html>
      <body>
        <h1>Hello!</h1>
        <p>This is an <strong>HTML</strong> email.</p>
      </body>
    </html>
    """

    message.attach(MIMEText(plain_text, "plain"))
    message.attach(MIMEText(html_text, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SENDER, [RECIPIENT], message.as_string())

        print("Email sent successfully.")

    except smtplib.SMTPException as exc:
        print(f"SMTP error while sending email: {exc}")
    except Exception as exc:
        print(f"Unexpected error while sending email: {exc}")


if __name__ == "__main__":
    send_html_email()