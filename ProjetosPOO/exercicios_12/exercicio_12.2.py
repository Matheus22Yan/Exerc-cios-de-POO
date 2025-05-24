entrada = "ABC431DEF901cC431203FXEW9"


def verifica_padrao(entrada, padroes):
    posicao = 0
    for padrao in padroes:
        achou, _, fim = padrao(entrada[posicao:])
        if achou > 0:
            posicao += fim + 1
        else:
            return -1, -1, -1
    return 1, 0, posicao - 1


def numeros(entrada):
    achados = 0
    fim = -1
    for i, caractere in enumerate(entrada):
        if "0" <= caractere <= "9":
            achados += 1
            fim = i
        else:
            break
    return achados, 0, fim


posicao = 0
while posicao < len(entrada):
    achado, inicio, fim = verifica_padrao(entrada[posicao:], [numeros])
    if achado > 0:
        print(entrada[posicao : posicao + fim + 1])
        posicao += fim + 1
    else:
        posicao += 1
