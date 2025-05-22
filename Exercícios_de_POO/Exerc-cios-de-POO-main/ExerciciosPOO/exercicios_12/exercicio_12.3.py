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


dois_numeros = partial(numero, qmin=2, qmax=2)
barra = partial(sequencia, padrao="/")
padrao = [dois_numeros, barra, dois_numeros, barra, dois_numeros]

entradas = [
    "12/03/24",
    "12/3/2024",
    "Dia doze de março 12/03",
    "12/03/24 12/03/2024 abc 21/30/24",
    "12/03/24 12/03/624 abc 21/30/24",
]
for entrada in entradas:
    print("Entrada:", entrada)
    achado = False
    posicao = 0
    while posicao < len(entrada):
        achou, inicio, fim = verifica_padrao(entrada[posicao:], padrao)
        if achou > 0:
            print(f"Data posições: {posicao+inicio} a {posicao+fim} ", end="")
            print("Data:", entrada[posicao + inicio : posicao + fim + 1])
            achado = True
            posicao += fim + 1
        else:
            posicao += 1
    if not achado:
        print("Nenhuma data encontrada na entrada")
    print()
