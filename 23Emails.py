# 2.3 Emails
class Email:
    def __init__(self, endereco, dominio):
        self.endereco = endereco
        self.dominio = dominio

def categorizar_email(email, regras):
    if email.dominio in regras['Spam']:
        return 'Spam'
    if email.dominio in regras['Trabalho']:
        return 'Trabalho'
    return 'Pessoal'

def classificar_emails(emails, regras):
    categorias = {'Pessoal': [], 'Trabalho': [], 'Spam': []}
    
    for email in emails:
        categoria = categorizar_email(email, regras)
        categorias[categoria].append(email.endereco)
    
    return categorias

if __name__ == "__main__":
    emails = [
        Email('john@example.com', 'example.com'),
        Email('sara@work.com', 'work.com'),
        Email('spam@mail.net', 'mail.net')
    ]

    regras = {
        'Spam': ['mail.net'],
        'Trabalho': ['work.com']
    }

    classificacao = classificar_emails(emails, regras)
    print(classificacao)
