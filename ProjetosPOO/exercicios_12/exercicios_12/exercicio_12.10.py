import re

REAIS_RE = r"^(([rR]\$)?(((\d{1,3}\.)?(\d{3}\.)*?\d{3})|(\d{1,3}))(,\d{2})?)$"
# ^ - Do começo da string
# ( - Grupo da parte direita da expressão, antes da vírgula
#  ([rR]\$)? - Opcionalmente pode ter o R$
#  ( - Grupo da parte inteira
#   ((\d{1,3}\.)?(\d{3}\.)*?\d{3}) - Grupo da parte inteira com pontos separando os milhares
#   Necessária para garantir que as partes entre os pontos tem 3 dígitos, salvo a primeira
#   | - ou
#   (\d{1,3}) - Grupo da parte inteira sem pontos
#  ) - Grupo da parte direita
# (,\d{2})? - Opcionalmente pode ter a parte decimal
# )$ - Até o fim da string


def limpa_espacos(entrada):
    return entrada.replace(" ", "")


def reais(entrada):
    # É mais fácil limpar os espaços antes de fazer a validação,
    # pois a expressão regular já é bem complexa
    # Lembre-se: você não precisa usar regex em tudo!
    entrada = limpa_espacos(entrada)
    return bool(re.match(REAIS_RE, entrada))


entradas = [
    "R$ 1.234,56",  # Sim
    "r$ 1.234,56",  # Sim
    "r$1.234,56",  # Sim
    "r$12.123.234,56",  # Sim
    "1.234,56",  # Sim
    "R$1.234,56",  # Sim
    "r$234,56",  # Sim
    "R$234,56",  # Sim
    "234,56",  # Sim
    "r$234",  # Sim
    "R$234",  # Sim
    "R$2",  # Sim
    "R$23",  # Sim
    "234",  # Sim
    "34",  # Sim
    "4",  # Sim
    "r$234,4",  # Não - Centavos tem que ter 2 dígitos
    "R$234,4",  # Não - Centavos tem que ter 2 dígitos
    "R$1234,4",  # Não - Sem o . para separar os milhares
    "r$1234,4",  # Não- Sem o . para separar os milhares
    "r$1234.12,4",  # Não - Uso incorreto do separador de milhares (.)
    "r$1.24,56",  # Não - Irregular, apenas dois números depois do .
]


for entrada in entradas:
    print(f"{entrada}: {reais(entrada)}")
