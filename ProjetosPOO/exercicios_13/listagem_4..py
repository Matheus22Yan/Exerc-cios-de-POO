import tkinter as tk
from tkinter import ttk


class Contador(ttk.Frame):
    def __init__(self, numero, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador = 0
        self.numero = numero
        self.label = ttk.Label(
            self, text=self.formata_contador(self.numero, self.contador)
        )
        self.label.pack()
        self.botao = ttk.Button(
            self, text=f"Adiciona ao contador {self.numero}", command=self.conta
        )
        self.botao.pack()
        self.pack()

    def formata_contador(self, contador, valor):
        return f"Contador {contador}: {valor}"

    def conta(self):
        self.contador += 1
        self.label["text"] = self.formata_contador(self.numero, self.contador)


class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contadores = []
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.botao = ttk.Button(
            self.quadro, text=f"Adiciona novo contador", command=self.adiciona_contador
        )
        self.botao.pack()
        self.quadro.pack(expand=True)

    def adiciona_contador(self):
        novo_contador = Contador(len(self.contadores) + 1, master=self.quadro)
        self.contadores.append(novo_contador)


raiz = Aplicacao()
raiz.mainloop()
