from datetime import date
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from modelo_site import Site
from data import Data


class Janela(tk.Toplevel):
    MIN_X = 300
    MIN_Y = 300
    PADXY = 10

    def __init__(self, parent, site, on_change=None):
        super().__init__(parent)
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.title("Site")
        self.padding = {"padx": self.PADXY, "pady": self.PADXY}
        self.on_change = on_change
        self.cria_controles()
        self.minsize(self.MIN_X, self.MIN_Y)
        self.captura_site(site)

    def captura_site(self, site):
        self.site = site or Site()
        self.url.set(self.site.url or "")
        self.data.set(self.site.data)
        self.categoria.set(self.site.categoria or "")
        self.t_notas.delete("1.0", tk.END)
        self.t_notas.insert("1.0", self.site.notas or "")

    def cria_controles(self):
        self.f_url = ttk.Frame(self)
        self.f_url.grid(row=0, column=0, columnspan=3, sticky=tk.EW, **self.padding)
        self.l_url = ttk.Label(self.f_url, text="URL")
        self.l_url.pack(anchor=tk.W)
        self.url = tk.StringVar()
        self.e_url = ttk.Entry(self.f_url, textvariable=self.url)
        self.e_url.pack(fill=tk.X, expand=True)
        self.f_categoria = ttk.Frame(self)
        self.f_categoria.grid(row=1, column=0, sticky=tk.W, **self.padding)
        self.l_categoria = ttk.Label(self.f_categoria, text="Categoria")
        self.l_categoria.pack(anchor=tk.W)
        self.categoria = tk.StringVar()
        self.e_categoria = ttk.Entry(self.f_categoria, textvariable=self.categoria)
        self.e_categoria.pack()
        self.f_data = ttk.Frame(self)
        self.f_data.grid(row=1, column=2, sticky=tk.E, **self.padding)
        self.l_data = ttk.Label(self.f_data, text="Data")
        self.l_data.pack(anchor=tk.W)
        self.data = Data(self.f_data)
        self.data.pack()
        self.f_notas = ttk.Frame(self)
        self.f_notas.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, **self.padding)
        self.l_notas = ttk.Label(self.f_notas, text="Notas")
        self.l_notas.pack(anchor=tk.W)
        self.t_notas = tk.Text(self.f_notas, height=3)
        self.t_notas.pack(expand=True, fill=tk.BOTH)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.b_frame = ttk.Frame(self)
        self.b_frame.grid(row=3, column=0, columnspan=3, **self.padding)
        self.b_ok = ttk.Button(self.b_frame, text="Ok", command=self.ok)
        self.b_ok.pack(side=tk.LEFT)
        self.b_cancelar = ttk.Button(self.b_frame, text="Cancelar", command=self.fecha)
        self.b_cancelar.pack(side=tk.LEFT)

    def fecha(self):
        self.destroy()

    def ok(self):
        try:
            self.valida_url()
        except ValueError:
            showerror("Erro", "URL inválida")
            return
        try:
            self.validar_data()
        except ValueError:
            showerror("Erro", "Data inválida")
            return
        self.site.url = self.url.get()
        self.site.categoria = self.categoria.get()
        self.site.data = self.data.get()
        self.site.notas = self.t_notas.get("1.0", tk.END)
        if self.on_change:
            self.on_change(self.site)
        self.fecha()

    def valida_url(self):
        if not self.url.get():
            raise ValueError("URL não pode ser vazia")

    def validar_data(self):
        dia, mês, ano = self.data.get().split("-")
        data = date(int(ano), int(mês), int(dia))
        return data
