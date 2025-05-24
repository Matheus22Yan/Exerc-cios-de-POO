# Programa 12,3: Reconhecendo o número do telefone
entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."
saida = []
telefone = []


def numero(entrada, qmin, qmax):
    num = 0
    for i, caractere in enumerate(entrada):
        if caractere.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return True, 0, num - 1
    return False, -1, -1


def ddd(entrada):
    estado = posicao = 0
    codigo_ddd = []
    while posicao < len(entrada):
        caractere = entrada[posicao]
        if estado == 0 and caractere == "(":
            estado = 1
            codigo_ddd.append(caractere)
        elif estado == 1:
            achou, inicio, fim = numero(entrada[posicao:], 2, 3)
            if achou:
                codigo_ddd.append(entrada[posicao + inicio : posicao + fim + 1])
                estado = 2
                posicao += fim
            else:
                break
        elif estado == 2:
            if caractere == ")":
                return True, 0, posicao
            break
        else:
            break
        posicao += 1
    return False, -1, -1


for posicao in range(len(entrada)):
    achou, inicio, fim = ddd(entrada[posicao:])
    if achou:
        print(f"DDD encontrado nas posições: {posicao + inicio} a {posicao + fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
