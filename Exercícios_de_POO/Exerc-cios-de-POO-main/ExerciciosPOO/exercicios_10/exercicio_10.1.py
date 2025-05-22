class Televisao:
    def __init__(self):
        self.ligada = False
        self.tamanho = 2
        self.tamanho = 20
        self.marca = "LG"


tv = Televisao()
tv.tamanho = 28
tv.marca = "SAMSUNG"

tv_sala = Televisao()
tv_sala.tamanho = 22
tv_sala.marca = "TCL"

print(f"Tamanho da Televisão:{tv.tamanho} Marca: {tv.marca}.")
print(f"Tamanho da Televisão da Sala = {tv_sala.tamanho} Marca: {tv_sala.marca}.")
 