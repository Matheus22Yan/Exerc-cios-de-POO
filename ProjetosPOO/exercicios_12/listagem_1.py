# Programa 12,2: Reconhecendo o DDD
entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."
saida = []
telefone = []


def ddd(entrada):
    estado = 0
    posicao_ddd = []
    for posicao, caractere in enumerate(entrada):
        if estado == 0 and caractere == "(":
            estado = 1
            posicao_ddd.append(caractere)
        elif estado == 1 and caractere.isnumeric() and posicao <= 3:
            posicao_ddd.append(caractere)
        elif estado == 1 and caractere == ")":
            estado = 2
            posicao_ddd.append(caractere)
            return True, 0, posicao
        else:
            break
    return False, -1, -1


for posicao in range(len(entrada)):
    achou, inicio, fim = ddd(entrada[posicao:])
    if achou:
        print(f"DDD encontrado nas posições; (posicao_ddd+inicio) a (posicao_ddd+fim)")
        print(entrada[posicao + inicio : posicao + fim + 1])
