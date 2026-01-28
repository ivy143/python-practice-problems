# Email Automation Script
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password):
    # Create the email headers and body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(login, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()
# Example usage
sender = "your_email@example.com"
receiver = "receiver_email@example.com"
subject = "Test Email from Automation Script"
body = "This is a test email sent from an automated Python script."
smtp_server = "smtp.example.com"
smtp_port = 587
login = "your_email@example.com"
password = "your_password"

send_email(sender, receiver, subject, body, smtp_server, smtp_port, login, password)
# This code sends an email using the smtplib library in Python.
# Make sure to replace the example email addresses, SMTP server details, and login credentials with your
# actual information before running the script.
# Note: For Gmail, you may need to enable "Less secure app access" or use an App Password if you have 2-Step Verification enabled.
# Ensure that you have internet access and the required libraries installed.
# You can install the required libraries using:
# pip install secure-smtplib email
# This script creates and sends an email with a subject and body text.