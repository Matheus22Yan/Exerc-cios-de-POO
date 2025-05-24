class Televisao:
    def __init__(self, canal_inicial, min, max):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisao(99,1,100)
print(f"Canal inicial: {tv.canal}")
print(f"Canal min: {tv.cmin}")
print(f"Canal max: {tv.cmax}")
tv.muda_canal_para_baixo()
print(f"O canal após baixar:{tv.canal}")
tv.muda_canal_para_cima()       
print(f"O canal após subir:{tv.canal}")       

        