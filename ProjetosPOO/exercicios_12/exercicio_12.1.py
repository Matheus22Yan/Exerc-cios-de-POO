entrada = "ABC431DEF901cC431203FXEW9"
saida = []
numero = []

for caractere in entrada:
    if "a" <= caractere.lower() <= "z":
        if not numero:
            saida.append(numero)
        numero += caractere
    elif numero:
        numero = []

for encontrado in saida:
    print("".join(encontrado))
