# Exemplo de dados (em um cenário real, você extrairia esses dados de suas fontes)
dados_visitas = [
    {'visitor_id': 'v1', 'page': '/home', 'duration': 5},
    {'visitor_id': 'v1', 'page': '/contact', 'duration': 2},
    {'visitor_id': 'v2', 'page': '/home', 'duration': 3},
    {'visitor_id': 'v3', 'page': '/products', 'duration': 8},
    {'visitor_id': 'v3', 'page': '/home', 'duration': 2},
]

# Análise de visitantes únicos
visitantes_unicos = set([visita['visitor_id'] for visita in dados_visitas])
print(f"Visitantes unicos: {len(visitantes_unicos)}")

# Análise de páginas mais visitadas
paginas_visitas = {}
for visita in dados_visitas:
    page = visita['page']
    paginas_visitas[page] = paginas_visitas.get(page, 0) + 1
pagina_mais_visitada = max(paginas_visitas, key=paginas_visitas.get)
print(f"Pagina mais visitada: {pagina_mais_visitada} ({paginas_visitas[pagina_mais_visitada]} visitas)")

# Análise da duração média da visita
duracao_total = sum([visita['duration'] for visita in dados_visitas])
duracao_media = duracao_total / len(dados_visitas)
print(f"Duracao media da visita: {duracao_media:.2f} minutos")
