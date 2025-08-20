Envío Automatizado de Correos a Centros Educativos
Este proyecto automatiza el envío masivo de solicitudes de prácticas educativas a diferentes centros, usando una hoja Excel con los datos personalizados de cada destinatario y el mensaje correspondiente. El sistema utiliza Python y conexión SMTP segura con Gmail mediante “Contraseña de aplicación”.

📑 Requisitos
Python 3.6 o superior

Paquetes Python: pandas, openpyxl

Cuenta Gmail con verificación en dos pasos (2FA) y contraseña de aplicación

⬇️ Instalación
Clona este repositorio:

bash
git clone https://github.com/tu-usuario/correo_centros_maes.git
cd correo_centros_maes
Instala las dependencias:

bash
pip install pandas openpyxl
⚙️ Configuración
1. Activa la verificación en dos pasos en tu cuenta Google.
2. Genera una contraseña de aplicación:
Accede a myaccount.google.com/security

Ve a “Contraseñas de aplicaciones” y sigue los pasos para obtener un código de 16 caracteres.

3. Prepara tu archivo correos_personalizados.xlsx
El archivo debe tener las siguientes columnas (puedes añadir más si lo necesitas):

Provincia	Localidad	Denominación Genérica	Denominación Específica	Código	Naturaleza	Teléfono	Correo	Correo Personalizado
Málaga	Málaga	Centro Docente Privado	Colegio Ejemplo	29000000	Centro concertado	952000000	ejemplo@colegio.com	Asunto: ... \n\n Estimado/a Responsable de prácticas, ...
La columna Correo Personalizado debe contener el asunto y el mensaje para cada destinatario, preferentemente en texto plano (puede tener saltos de línea y variables personalizadas).

📝 Ejemplo de configuración del script
Asegúrate de modificar las variables de correo al inicio de tu archivo Python, por ejemplo:

python
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Cargar datos
df = pd.read_excel('correos_personalizados.xlsx')

# Configuración del remitente
correo_emisor = 'tucuenta@gmail.com'
password_emisor = 'contraseña_de_aplicacion_16_caracteres'

# SMTP Gmail
smtp_host = 'smtp.gmail.com'
smtp_port = 587

for i, row in df.iterrows():
    destinatario = row['Correo']
    mensaje = row['Correo Personalizado']
    # Separar asunto y cuerpo si es necesario
    if mensaje.startswith("Asunto:"):
        split_msg = mensaje.split('\n', 1)
        asunto = split_msg[0].replace("Asunto:", "").strip()
        cuerpo = split_msg[1] if len(split_msg) > 1 else ""
    else:
        asunto = ""
        cuerpo = mensaje

    msg = MIMEText(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = correo_emisor
    msg['To'] = destinatario

    # Enviar correo
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(correo_emisor, password_emisor)
        server.sendmail(correo_emisor, destinatario, msg.as_string())
🚀 Uso
Asegúrate de tener preparado tu correos_personalizados.xlsx con la estructura indicada.

Ejecuta el script:

bash
python automatiza_envios.py
Consulta la terminal para incidencias o confirmaciones de envío.

🛡️ Seguridad
No subas tu contraseña de aplicación ni datos sensibles a repositorios públicos.

Usa variables de entorno para proteger tus credenciales si compartes el script.

🖇️ Créditos
Desarrollado por Daniel Rodríguez Carrión.

¿Dudas?
Si tienes alguna consulta, abre un Issue o contacta al desarrollador.


*******************


Automated Email Sending to Educational Institutions
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
