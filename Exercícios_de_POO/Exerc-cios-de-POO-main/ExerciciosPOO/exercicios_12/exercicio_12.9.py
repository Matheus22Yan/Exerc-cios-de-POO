import re

CPF_RE = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
# \d{3}	Três dígitos
# \.	Ponto literal
# \d{3}	Três dígitos
# \.	Ponto literal
# \d{3}	Três dígitos
# -	Traço literal
# \d{2}	Dois dígitos finais (DV)
# ^...$	Começo e fim da string
CNPJ_RE = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
# \d{2}	Dois dígitos iniciais
# \.	Ponto literal
# \d{3}	Três dígitos
# \.	Ponto literal
# \d{3}	Três dígitos
# /	Barra literal
# \d{4}	Quatro dígitos (filial)
# -	Traço literal
# \d{2}	Dois dígitos finais (DV)


def cpf(entrada):
    return bool(re.match(CPF_RE, entrada))


# Verifica se entrada é um CNPJ válido, ou seja:
# Uma sequência no formato 99.999.999/9999-99
def cnpj(entrada):
    return bool(re.match(CNPJ_RE, entrada))


entradas = [
    "12.345.678/9012-34",  # CNPJ válido
    "12.345.678-9012-34",  # Inválido
    "99.999.999/9999-99",  # CNPJ válido
    "123.456.789-01",  # CPF válido
    "23.456.789-01",  # Inválido
    "999.456.789-01",  # CPF válido
]

for entrada in entradas:
    print(
        f"{entrada}:\né um CNPJ? {'Sim' if cnpj(entrada) else 'Não'}\né um CPF? {'Sim' if cpf(entrada) else 'Não'}\n"
    )
