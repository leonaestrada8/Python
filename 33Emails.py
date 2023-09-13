#3.3 Emails

def filter_critical_events(logs):
    return [log for log in logs if log.startswith("CRITICAL")]

def generate_report(logs):
    critical_events = filter_critical_events(logs)

    if not critical_events:
        print("Nenhum evento critico encontrado.")
        return

    print("Relatorio de Eventos Criticos:")
    for event in critical_events:
        print(event)

if __name__ == "__main__":
    logs = [
        "INFO: Usuário logado com sucesso.",
        "CRITICAL: Falha na base de dados.",
        "INFO: Arquivo atualizado.",
        "WARNING: Tentativa de acesso não autorizado.",
        "CRITICAL: Sistema de arquivos corrompido.",
    ]

    generate_report(logs)
