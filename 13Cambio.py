# Definindo taxas de câmbio fixas
usd_para_brl = 5.2
eur_para_brl = 6.1
usd_para_eur = eur_para_brl / usd_para_brl

valor = float(input("Informe o valor a ser convertido: "))
moeda_origem = input("Informe a moeda de origem (USD, EUR, BRL): ").upper()
moeda_destino = input("Informe a moeda de destino (USD, EUR, BRL): ").upper()

valor_convertido = 0.0

# Convertendo o valor de acordo com as moedas selecionadas
if moeda_origem == "USD" and moeda_destino == "BRL":
    valor_convertido = valor * usd_para_brl
elif moeda_origem == "USD" and moeda_destino == "EUR":
    valor_convertido = valor * usd_para_eur
elif moeda_origem == "EUR" and moeda_destino == "BRL":
    valor_convertido = valor * eur_para_brl
elif moeda_origem == "EUR" and moeda_destino == "USD":
    valor_convertido = valor / usd_para_eur
elif moeda_origem == "BRL" and moeda_destino == "USD":
    valor_convertido = valor / usd_para_brl
elif moeda_origem == "BRL" and moeda_destino == "EUR":
    valor_convertido = valor / eur_para_brl

print(f"Valor convertido: {moeda_destino} {valor_convertido}")
