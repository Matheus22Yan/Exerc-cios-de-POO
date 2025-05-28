# Programa 12.4; Programa modificado para reconhecer sequências
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
    posicao, posicao_maxima = 0, len(padrao)
    for caractere in entrada:
        if caractere == padrao[posicao]:
            posicao += 1
        else:
            break
        if posicao == posicao_maxima:
            return 1, 0, posicao - 1
    return -1, -1, -1


def ddd(entrada):
    achou, _, _ = sequencia(entrada[0], "(")
    if achou > 0:
        achou, _, n_fim = numero(entrada[1:], 2, 3)
        if achou > 0:
            achou, _, _ = sequencia(entrada[n_fim + 2], ")")
            if achou > 0:
                return 1, 0, achou + 2
    return -1, -1, -1


for posicao in range(len(entrada)):
    achou, inicio, fim = ddd(entrada[posicao:])
    if achou > 0:
        print(f"DDD encontrado nas posições: {posicao + inicio} a {posicao + fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
