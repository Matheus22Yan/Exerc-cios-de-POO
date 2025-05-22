from functools import partial


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


def opcional(entrada, padroes):
    achou, inicio, fim = verifica_padrao(entrada, padroes)
    if achou > 0:
        return achou, inicio, fim
    else:
        return 1, -1, -1


tres_numeros = partial(numero, qmin=1, qmax=3)
centavos = partial(numero, qmin=1, qmax=2)
cifrao = partial(sequencia, padrao="R$")
virgula = partial(sequencia, padrao=",")

padrao = [cifrao, tres_numeros, virgula, centavos]
# padrao = [cifrao, tres_numeros, partial(opcional, padroes=[virgula, centavos])]

entradas = [
    "R$123,45",
    "R$123,450",
    "$123,45",
    "R$12,34",
    "R$123,45 R$12,34 R$1,23 R$1,0",
    "R$123 R$12 R$1 R$1,0",
]
for entrada in entradas:
    print("Entrada:", entrada)
    achado = False
    posicao = 0
    while posicao < len(entrada):
        achou, inicio, fim = verifica_padrao(entrada[posicao:], padrao)
        if achou > 0:
            print(f"Reais nas posições: {posicao+inicio} a {posicao+fim} ", end="")
            print("Reais:", entrada[posicao + inicio : posicao + fim + 1])
            achado = True
            posicao += fim + 1
        else:
            posicao += 1
    if not achado:
        print("Nenhum valor em reais encontrado na entrada")
    print()
