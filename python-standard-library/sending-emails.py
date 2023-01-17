import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
import os

def send_simple_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Create the email message
        message = f"Subject: {subject}\n\n{body}"
        
        # Create SMTP session
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Enable TLS
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        
        print("Simple email sent successfully")
    except Exception as e:
        print(f"Error sending simple email: {e}")

def send_html_email(sender_email, sender_password, receiver_email, subject, html_content):
    try:
        # Create multipart message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Add HTML content
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)

        # Create SMTP session
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        print("HTML email sent successfully")
    except Exception as e:
        print(f"Error sending HTML email: {e}")

def send_email_with_attachment(sender_email, sender_password, receiver_email, 
                             subject, body, attachment_path):
    try:
        # Create multipart message
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Add body
        message.attach(MIMEText(body, "plain"))

        # Add attachment
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            
        # Encode attachment
        encoders.encode_base64(part)
        
        # Add header
        filename = Path(attachment_path).name
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message
        message.attach(part)

        # Create SMTP session
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        print("Email with attachment sent successfully")
    except Exception as e:
        print(f"Error sending email with attachment: {e}")

# Example usage (commented out as it requires real credentials)
"""
# Email credentials
sender_email = "your_email@gmail.com"
sender_password = "your_app_specific_password"  # Use App-Specific Password
receiver_email = "recipient@example.com"

# Send simple email
send_simple_email(
    sender_email,
    sender_password,
    receiver_email,
    "Test Subject",
    "This is a test email from Python."
)

# Send HTML email
html_content = '''
<html>
    <body>
        <h1>Hello from Python!</h1>
        <p>This is an <b>HTML</b> email.</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </body>
</html>
'''
send_html_email(
    sender_email,
    sender_password,
    receiver_email,
    "HTML Test Email",
    html_content
)

# Send email with attachment
send_email_with_attachment(
    sender_email,
    sender_password,
    receiver_email,
    "Email with Attachment",
    "Please find the attachment.",
    "document.pdf"
)
""" 