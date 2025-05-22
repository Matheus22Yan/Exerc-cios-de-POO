import tkinter as tk 
from tkinter import ttk

class Aplicacao(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_1 = 0
        self.contador_2 = 0
        self.title("Contadores")
        self.geometry("250x100")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_contador_1 = ttk.Label(
            self.quadro, text=self.formata_contador(1, self.contador_1))
        self.l_contador_1.pack()
        self.botao_1 = ttk.Button(
            self.quadro, text="Adiciona ao contador 1", command=self.conta_1)  
        