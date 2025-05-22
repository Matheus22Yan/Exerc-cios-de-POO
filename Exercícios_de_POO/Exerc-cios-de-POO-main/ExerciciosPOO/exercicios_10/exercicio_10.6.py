class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
        return self.canal

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
        return self.canal                    
        
tv = Televisao(1,5)
print(f"Canal atual: {tv.canal}")
print(f"Canal atual após baixar: {tv.muda_canal_para_baixo()}")
print(f"Canal atual após subir: {tv.muda_canal_para_cima()}") 

