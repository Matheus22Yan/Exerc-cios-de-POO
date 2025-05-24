# Programa 12.5: Usando uma lista de funções a aplicar
from functools import partial

entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."


def numero(entrada, qmin, qmax):
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


def sequencia(entrada, padrao):
    posicao, posicao_max = 0, len(padrao)
    for caractere in entrada:
        if caractere == padrao[posicao]:
            posicao += 1
        else:
            break
        if posicao == posicao_max:
            return 1, 0, posicao - 1
    return -1, -1, -1


def verifica_padrao(entrada, padroes):
    posicao = 0
    for padrao in padroes:
        achou, _, fim = padrao(entrada[posicao:])
        if achou > 0:
            posicao += fim + 1
        else:
            return -1, -1, -1
    return 1, 0, posicao - 1


def ddd(entrada):
    achou, _, fim = verifica_padrao(
        entrada,
        [
            partial(sequencia, padrao="("),
            partial(numero, qmin=2, qmax=3),
            partial(sequencia, padrao=")"),
        ],
    )
    return (1, 0, fim) if achou > 0 else (-1, -1, -1)


def telefone(entrada):
    return verifica_padrao(
        entrada,
        [
            partial(ddd),
            partial(numero, qmin=4, qmax=4),
            partial(sequencia, padrao="-"),
            partial(numero, qmin=4, qmax=4),
        ],
    )


for posicao in range(len(entrada)):
    achou, inicio, fim = telefone(entrada[posicao:])
    if achou > 0:
        print(f"Telefone encontrado nas posições: {posicao + inicio} a {posicao+fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
