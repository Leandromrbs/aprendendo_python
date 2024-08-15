import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = "smtp-mail.outlook.com"
port = 587  # Porta para TLS
login = "lmorais@sescpe.com.br"
password = "P@ntera6040"

# Configuração do e-mail
sender_email = "lmorais@sescpe.com.br"
receiver_email = "leandromrbs@hotmail.com"
subject = "Assunto do E-mail"
body = "Este é um e-mail enviado automaticamente pelo Python!"

# Criação da mensagem
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Envio do e-mail
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Segurança
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
finally:
    server.quit()
