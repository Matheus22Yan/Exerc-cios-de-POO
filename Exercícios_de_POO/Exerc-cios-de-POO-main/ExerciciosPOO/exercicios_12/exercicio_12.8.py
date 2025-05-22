import re

CNPJ_RE = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
# # ^	Início da string
# \d{2}	Dois dígitos (primeiro bloco)
# \.	Um ponto literal (escapado com \)
# \d{3}	Três dígitos (segundo bloco)
# \.	Outro ponto literal
# \d{3}	Três dígitos (terceiro bloco)
# /	Uma barra / literal
# \d{4}	Quatro dígitos (quarto bloco)
# -	Um traço - literal
# \d{2}	Dois dígitos (dígitos verificadores)
# $	Final da string


# Verifica se entrada é um CNPJ válido, ou seja:
# Uma sequência no formato 99.999.999/9999-99
def cnpj(entrada):
    return bool(re.match(CNPJ_RE, entrada))


entradas = [
    "12.345.678/9012-34",  # Sim
    "12.345.678-9012-34",  # Não
    "12.345.678.9012-34",  # Não
    "2.345.678/9012-34",  # Não
    "12.345.678/9012-4",  # Não
    "99.999.999/9999-99",  # Sim
]

for entrada in entradas:
    print(f"{entrada}: é um CNPJ? {'Sim' if cnpj(entrada) else 'Não'}")
