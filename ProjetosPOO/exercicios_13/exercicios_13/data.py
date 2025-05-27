import tkinter as tk
import tkinter.ttk as ttk


class Data(ttk.Frame):
    def __init__(self, parent, min_ano=00, max_ano=40):
        super().__init__(parent)
        self.min_ano = min_ano
        self.max_ano = max_ano
        self.dia = tk.StringVar()
        self.mês = tk.StringVar()
        self.ano = tk.StringVar()
        self.cria_controles()

    def set(self, data):
        dia, mês, ano = data.split("-")
        self.dia.set(dia)
        self.mês.set(mês)
        self.ano.set(ano)

    def get(self):
        return f"{self.dia.get()}-{self.mês.get()}-{self.ano.get()}"

    def cria_controles(self):
        self.c_dia = ttk.Combobox(
            self,
            textvariable=self.dia,
            width=3,
            values=[f"{d:02d}" for d in range(1, 32)],
            state="readonly",
        )
        self.c_dia.pack(side=tk.LEFT)
        self.c_mes = ttk.Combobox(
            self,
            textvariable=self.mês,
            values=[f"{m:02d}" for m in range(1, 13)],
            width=3,
            state="readonly",
        )
        self.c_mes.pack(side=tk.LEFT)
        self.c_ano = ttk.Combobox(
            self,
            textvariable=self.ano,
            values=[f"{m:02d}" for m in range(self.min_ano, self.max_ano + 1)],
            width=6,
            state="readonly",
        )
        self.c_ano.pack(side=tk.LEFT)
