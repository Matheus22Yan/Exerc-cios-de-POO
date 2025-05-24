from functools import partial


def número(entrada, qmin, qmax):
    num = 0
    for caractere in entrada:
        if caractere.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return num, 0, num - 1
    else:
        return -1, -1, -1


def sequência(entrada, padrão):
    posição, posição_max = 0, len(padrão)
    for caractere in entrada:
        if caractere == padrão[posição]:
            posição += 1  # Caracteres iguais, testa o próximo caractere
        else:
            break  # Saiu da sequência
        if posição == posição_max:  # Achou toda a sequência
            return 1, 0, posição - 1
    return -1, -1, -1


def verifica_padrão(entrada, padrões):
    posição = 0
    for padrão in padrões:
        achou, _, fim = padrão(entrada[posição:])
        if achou > 0:
            posição += fim + 1
        else:
            return -1, -1, -1
    return 1, 0, posição - 1


def numero_celular(entrada):
    padrão = [
        partial(sequência, padrão="("),
        partial(número, qmin=2, qmax=3),
        partial(sequência, padrão=")"),
        partial(número, qmin=5, qmax=5),
        partial(sequência, padrão="-"),
        partial(número, qmin=4, qmax=4),
    ]
    achou, _, _ = verifica_padrão(entrada, padrão)
    return achou > 0


entradas = [
    "(92)99999-9999",  # Sim
    "(11)99999-999",  # Não
    "(2)99999-9999",  # Não
    "(12)9999999999",  # Não
    "(312)9999999999",  # Não
    "(312)99999-9999",  # Sim
]

for entrada in entradas:
    print(f"{entrada}: é um celular? {'Sim' if numero_celular(entrada) else 'Não'}")
