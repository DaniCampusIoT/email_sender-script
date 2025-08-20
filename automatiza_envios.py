import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Ruta al archivo con correos personalizados
archivo_excel = 'correos_personalizados.xlsx'

# Ruta a tu CV en PDF para adjuntar en el correo
archivo_cv = 'your_cv.pdf'  # Cambia esto por la ruta correcta de tu CV

# Configuración SMTP
smtp_servidor = 'smtp.gmail.com'
smtp_puerto = 587
correo_emisor = 'your_email@gmail.com'         # Cambia por tu correo
password_emisor = 'your_app_password' # Cambia por tu contraseña o app password

# Función para enviar correo con adjunto CV
def enviar_correo(destinatario, asunto, cuerpo, ruta_adjunto=None):
    msg = MIMEMultipart()
    msg['From'] = correo_emisor
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Especifica codificación utf-8 en el MIMEText
    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    if ruta_adjunto:
        with open(ruta_adjunto, 'rb') as f:
            part = MIMEApplication(f.read(), Name=ruta_adjunto)
        part['Content-Disposition'] = f'attachment; filename="{ruta_adjunto}"'
        msg.attach(part)

    try:
        servidor = smtplib.SMTP(smtp_servidor, smtp_puerto)
        servidor.starttls()
        servidor.login(correo_emisor, password_emisor)
        servidor.send_message(msg)
        servidor.quit()
        print(f'Correo enviado a: {destinatario}')
    except Exception as e:
        print(f'Error enviando correo a {destinatario}: {e}')

# Leer datos
df = pd.read_excel(archivo_excel)

for idx, fila in df.iterrows():
    correo_destino = fila['Correo']
    texto_completo = fila['Correo Personalizado']
    
    # Separar asunto y cuerpo
    lines = texto_completo.splitlines()
    asunto_line = next((linea for linea in lines if linea.strip().lower().startswith('asunto:')), None)
    if asunto_line:
        asunto = asunto_line[len('Asunto:'):].strip()
        # El cuerpo va desde la línea siguiente al asunto hasta el final
        cuerpo = '\n'.join(lines[lines.index(asunto_line) + 1:]).strip()
    else:
        asunto = 'Solicitud de prácticas educativas'
        cuerpo = texto_completo
    
    enviar_correo(correo_destino, asunto, cuerpo, ruta_adjunto=archivo_cv)
