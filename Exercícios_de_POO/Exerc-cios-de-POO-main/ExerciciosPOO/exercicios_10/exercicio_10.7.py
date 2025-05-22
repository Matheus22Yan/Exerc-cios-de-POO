class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if not self.ligada:
            print(f"Não está ligada para mexer")
            return 
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if not self.ligada:
            print(f"Não está ligada para mexer")
            return 
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = Televisao(2,3)
tv.ligada = True
print(f"Canal atual: {tv.canal}")  
tv.muda_canal_para_baixo()
print(f"Canal atual: {tv.canal}")
tv.muda_canal_para_cima()
print(f"Canal atual: {tv.canal}")



