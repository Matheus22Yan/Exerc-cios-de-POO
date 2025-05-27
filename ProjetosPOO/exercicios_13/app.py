import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion, showinfo
from gerente import GerenteDeSites
from janela import Janela
import os


class App(tk.Tk):
    MIN_X = 800
    MIN_Y = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Controle de sites interessantes")
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.cria_controles()
        self.gerente = GerenteDeSites()
        caminho_json = os.path.join(os.path.dirname(__file__), "dados.json")
        self.gerente.carrega(caminho_json)
        self.mostra_dados()
        self.minsize(self.MIN_X, self.MIN_Y)

    def cria_controles(self):
        self.quadro = ttk.Frame(self)
        self.quadro.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW
        )
        self.grid_rowconfigure(0, weight=1)
        self.tabela = ttk.Treeview(
            self.quadro, columns=["url", "categoria", "data", "notas"], show="headings"
        )
        self.tabela.heading("url", text="URL")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.column("categoria", anchor=tk.CENTER)
        self.tabela.heading("data", text="Data")
        self.tabela.column("data", anchor=tk.CENTER)
        self.tabela.heading("notas", text="Notas")
        self.tabela.grid(row=0, column=0, sticky=tk.NSEW)
        self.tabela.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(
            self.quadro, orient=tk.VERTICAL, command=self.tabela.yview
        )
        self.tabela.configure(yscroll=scrollbar.set)
        self.tabela.bind("<Double-Button-1>", self.abre_janela)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.quadro.grid_columnconfigure(0, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.quadro.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.menu = tk.Menu(self)
        self.m_arquivo = tk.Menu(self.menu, tearoff=0)
        self.m_arquivo.add_command(label="Ler", command=self.lê)
        self.m_arquivo.add_command(label="Gravar", command=self.grava)
        self.m_sites = tk.Menu(self.menu, tearoff=0)
        self.m_sites.add_command(label="Adiciona", command=self.adiciona)
        self.m_sites.add_command(label="Apaga", command=self.apaga)
        self.m_sites.add_separator()
        self.m_sites.add_command(label="Apaga todos", command=self.apaga_todos)
        self.menu.add_cascade(label="Arquivo", menu=self.m_arquivo)
        self.menu.add_cascade(label="Sites", menu=self.m_sites)
        self.menu.add_command(label="Sobre", command=self.sobre)
        self.config(menu=self.menu)

    def adiciona(self):
        self.mostra_site(None)

    def apaga(self):
        if id_selecionado := self.pega_selecionado():
            del self.gerente.sites[id_selecionado]
            self.tabela.delete(id_selecionado)

    def apaga_todos(self):
        if (
            askquestion(
                title="Apagar todos os sites", message="Confirma apagar todos os sites?"
            )
            == "yes"
        ):
            self.limpa()

    def limpa(self):
        self.gerente.sites.clear()
        self.tabela.delete(*self.tabela.get_children())

    def sobre(self):
        showinfo(
            title="Sobre",
            message="Introdução à Programação com Python.\nhttps://python.nilo.pro.br",
        )

    def lê(self):
        if nome := askopenfilename(filetypes=[("JSON", "*.json")]):
            self.limpa()
            self.gerente.carrega(nome)
            self.mostra_dados()

    def grava(self):
        if nome := asksaveasfilename(
            filetypes=[("JSON", "*.json")], defaultextension=".json"
        ):
            self.gerente.grava(nome)

    def adiciona_site_a_tabela(self, site):
        self.tabela.insert(
            "",
            tk.END,
            values=(site.url, site.categoria, site.data, site.notas),
            iid=site.id,
        )

    def mostra_dados(self):
        for site in self.gerente.sites.values():
            self.adiciona_site_a_tabela(site)

    def pega_selecionado(self):
        if item_selecionado := self.tabela.selection():
            id_selecionado = item_selecionado[0]
            return id_selecionado
        return None

    def abre_janela(self, event):
        if id_selecionado := self.pega_selecionado():
            site = self.gerente.sites[id_selecionado]
        else:
            site = None
        self.mostra_site(site)

    def mostra_site(self, site):
        self.janela = Janela(self, site, on_change=self.atualiza)
        self.janela.grab_set()

    def atualiza(self, site):
        if self.tabela.exists(site.id):
            self.tabela.item(
                site.id,
                text="",
                values=(site.url, site.categoria, site.data, site.notas),
            )
        else:
            self.adiciona_site_a_tabela(site)
        self.gerente.sites[site.id] = site


App().mainloop()
