class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >=self.cmin:
            self.canal -= 1

        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = Televisao(2,10)
tv.muda_canal_para_baixo()
print(f"Canal da Tv: {tv.canal}")                           
tv.muda_canal_para_cima()
print(f"Canal da Tv: {tv.canal}")