import os.path
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askquestion, showinfo, showerror

from uuid import uuid4
from datetime import date

# Todas as classes estão incluídas na resposta do exercício
# Apenas a classe App foi alteradas e
# a classe GerenteDeSitesDB foi criada


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


class Site:
    def __init__(self, /, url=None, categoria=None, data=None, id=None, notas=None):
        if id is None:
            id = str(uuid4())
        self.id = id
        if data is None:
            data = date.today().strftime("%d-%m-%y")
        self.data = data
        self.url = url
        self.categoria = categoria
        self.notas = notas

    def __str__(self):
        return f"Site {self.id} {self.url} {self.categoria} {self.notas}"


class GerenteDeSitesDB:
    def __init__(self):
        self.nome = "agenda.db"
        existe = os.path.exists(self.nome)
        self.conecta()
        if not existe:
            self.cria_tabela()

    def cria_tabela(self):
        self.conexão.execute(
            "CREATE TABLE sites (id TEXT PRIMARY KEY, url TEXT, categoria TEXT, data TEXT, notas TEXT)"
        )
        self.conexão.commit()

    def conecta(self):
        self.conexão = sqlite3.connect(self.nome)

    def desconecta(self):
        self.conexão.close()

    def salva(self, site):
        self.conexão.execute(
            """INSERT INTO sites (id, url, categoria, data, notas) VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET url=excluded.url, categoria=excluded.categoria, data=excluded.data, notas=excluded.notas""",
            (site.id, site.url, site.categoria, site.data, site.notas),
        )
        self.conexão.commit()
        self.sites[site.id] = site

    def apaga(self, id):
        self.conexão.execute("DELETE FROM sites WHERE id=?", (id,))
        self.conexão.commit()
        if id in self.sites:
            del self.sites[id]

    def carrega(self):
        self.sites = {}
        q = self.conexão.execute("SELECT * FROM sites")
        for site in q.fetchall():
            novo_site = Site(
                id=site[0],
                url=site[1],
                categoria=site[2],
                data=site[3],
                notas=site[4],
            )
            self.sites[novo_site.id] = novo_site
        return self.sites


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
        except ValueError as e:
            showerror("Erro", f"URL inválida\n{e}")
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
        url = self.url.get()
        if not url:
            raise ValueError("URL não pode ser vazia")
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError("URL deve começar com http:// ou https://")

    def validar_data(self):
        dia, mês, ano = self.data.get().split("-")
        data = date(int(ano), int(mês), int(dia))
        return data


class App(tk.Tk):
    MIN_X = 800
    MIN_Y = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Controle de sites interessantes")
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.cria_controles()
        self.gerente = GerenteDeSitesDB()
        self.gerente.carrega()
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
        # self.m_arquivo = tk.Menu(self.menu, tearoff=0)
        # self.m_arquivo.add_command(label="Ler", command=self.lê)
        # self.m_arquivo.add_command(label="Gravar", command=self.grava)
        self.m_sites = tk.Menu(self.menu, tearoff=0)
        self.m_sites.add_command(label="Adiciona", command=self.adiciona)
        self.m_sites.add_command(label="Apaga", command=self.apaga)
        self.m_sites.add_separator()
        self.m_sites.add_command(label="Apaga todos", command=self.apaga_todos)
        # self.menu.add_cascade(label="Arquivo", menu=self.m_arquivo)
        self.menu.add_cascade(label="Sites", menu=self.m_sites)
        self.menu.add_command(label="Sobre", command=self.sobre)
        self.config(menu=self.menu)

    def adiciona(self):
        self.mostra_site(None)

    def apaga(self):
        if id_selecionado := self.pega_selecionado():
            self.gerente.apaga(id_selecionado)
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
        for id in self.gerente.sites.keys():
            self.gerente.apaga(id)
        self.gerente.sites.clear()
        self.tabela.delete(*self.tabela.get_children())

    def sobre(self):
        showinfo(
            title="Sobre",
            message="Introdução à Programação com Python.\nhttps://python.nilo.pro.br",
        )

    def adiciona_site_a_tabela(self, site):
        self.gerente.salva(site)
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
        self.gerente.salva(site)


App().mainloop()
