# Automated Email Sending to Educational Institutions
This project automates the bulk sending of internship request emails to educational centers using an Excel file containing personalized data for each recipient and their corresponding message. The system uses Python and secure SMTP connection with Gmail via an App Password.

📑 Requirements
Python 3.6 or higher

Python packages: pandas, openpyxl

Gmail account with 2-step verification (2FA) enabled and an App Password

⬇️ Installation
Clone this repository:

text
git clone https://github.com/your-username/correo_centros_maes.git
cd correo_centros_maes
Install dependencies:

text
pip install pandas openpyxl
⚙️ Configuration
1. Enable 2-Step Verification (2FA) on your Google account.

2. Generate an App Password:

Go to https://myaccount.google.com/security

Under “App passwords”, follow the steps to get your 16-character code.

3. Prepare your correos_personalizados.xlsx file

Your Excel file should include the following columns:

Province	City	Generic Name	Specific Name	Code	Type	Phone	Email	Personalized Email
Málaga	Málaga	Private School Center	Example School	29000000	Associated Center	952000000	example@school.com	Subject: ... \n\n Dear ... (message)
The Personalized Email column should contain the subject and body for each recipient (plain text, can have line breaks).

📝 Example: Script Configuration
Update your Python script with the following variables at the beginning:

text
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Load data
df = pd.read_excel('correos_personalizados.xlsx')

# Sender configuration
sender_email = 'youraddress@gmail.com'
sender_password = 'your_16_character_app_password'

# Gmail SMTP server
smtp_host = 'smtp.gmail.com'
smtp_port = 587

for i, row in df.iterrows():
    recipient = row['Email']
    message = row['Personalized Email']
    # Separate subject and body if needed
    if message.startswith("Subject:"):
        split_msg = message.split('\n', 1)
        subject = split_msg[0].replace("Subject:", "").strip()
        body = split_msg[1] if len(split_msg) > 1 else ""
    else:
        subject = ""
        body = message

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    # Send email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
🚀 Usage
Make sure your correos_personalizados.xlsx is properly formatted.

Run the script:

text
python automatiza_envios.py
Check the terminal for confirmation or error messages.

🛡️ Security
Never upload your app password or sensitive information to public repositories.

Use environment variables or secure config files for your credentials if sharing code.

🖇️ Credits
Developed by Daniel Rodríguez Carrión.

Questions?
If you have any issues, open an Issue or contact the developer.
