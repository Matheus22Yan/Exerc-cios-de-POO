import re

CPF_RE = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
# ^	 Início da string
# \d{3}	Três dígitos (primeiro bloco do CPF)
# \.	Um ponto literal (precisa escapar com \)
# \d{3}	Três dígitos (segundo bloco)
# \.	Outro ponto literal
# \d{3}	Três dígitos (terceiro bloco)
# -	Traço literal
# \d{2}	Dois dígitos (dígitos verificadores)
# $	Fim da string


def cpf(entrada):
    return bool(re.match(CPF_RE, entrada))


entradas = [
    "123.456.789-01",  # Sim
    "123456.789-01",  # Não
    "123.456.78901",  # Não
    "23.456.789-01",  # Não
    "123.456.78-01",  # Não
    "999.999.999-99",  # Sim
]

for entrada in entradas:
    print(f"{entrada}: é um CPF? {'Sim' if cpf(entrada) else 'Não'}")
