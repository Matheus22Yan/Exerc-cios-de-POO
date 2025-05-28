from functools import partial


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


def sequências(entrada, padrão, qmin=1, qmax=1):
    posição = 0
    fim = -1
    achados = 0
    while posição < len(entrada):
        achou, _, ifim = sequência(entrada[posição:], padrão)
        if achou > 0:
            achados += 1
            posição += ifim + 1
            fim = posição - 1
        else:
            break
    # Caso o padrão seja opcional, retorna achado 1, mas inicio e fim -1
    # para que verifica_padrão continue procurando
    if qmin == 0 and achados == 0:
        return 1, -1, -1
    # Verifica se o número de achos está entre qmain e qmax
    elif qmin <= achados <= qmax:
        return achados, 0, fim
    else:
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


entradas = [
    "(((---)))",  # Padrão encontrado
    "(((--)))",  # Padrão não encontrado
    "(----)",  # Padrão não encontrado
    "----",  # Padrão não encontrado
    "((--))",  # Padrão não encontrado
    "<(((--)))>",  # Padrão encontrado
    "<<(((--)))>>",  # Padrão encontrado
    "<<(((---)))>>",  # Padrão encontrado
    "<<((--))>> <(((---)))> (((---))) ((((----))))",  # Padrão encontrado duas vezes
]
# O padrão é uma sequência de caracteres que podem ser opcionais
# < zero ou até duas vezes
# ( três ou até quatro vezes
# - duas ou até três vezes
# ) três ou até quatro vezes
# > zero ou até duas vezes
# Você pode criar outros padrões para testar a função sequências
padrão = [
    partial(sequências, padrão="<", qmin=0, qmax=2),
    partial(sequências, padrão="(", qmin=3, qmax=4),
    partial(sequências, padrão="-", qmin=2, qmax=3),
    partial(sequências, padrão=")", qmin=3, qmax=4),
    partial(sequências, padrão=">", qmin=0, qmax=2),
]

for entrada in entradas:
    print("Entrada:", entrada)
    achado = False
    posição = 0
    while posição < len(entrada):
        achou, início, fim = verifica_padrão(entrada[posição:], padrão)
        if achou > 0:
            print(f"Padrão nas posições: {posição+início} a {posição+fim} ", end="")
            print("Padrão:", entrada[posição + início : posição + fim + 1])
            achado = True
            posição += fim + 1
        else:
            posição += 1
    if not achado:
        print("Nenhum padrão encontrado na entrada")
    print()
