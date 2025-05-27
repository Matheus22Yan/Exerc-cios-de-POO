import tkinter as tk
import tkinter.ttk as ttk
import json
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cor_de_fundo = ""
        self.cor_de_frente = "black"
        self.quadro = tk.Frame(self)
        self.cria_barra()
        self.cria_area_de_desenho()
        self.title("Desenho")
        self.geometry("1200x700")
        self.cruz = []
        self.cruz.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.cruz.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.estado = 0
        self.xi = None
        self.yi = None
        self.curr_id = 0
        self.quadro.pack(expand=True, fill=tk.BOTH)
        self.ferramenta = self.canvas.create_line

    def cria_area_de_desenho(self):
        self.trabalho = tk.Frame(self.quadro, height=600)
        self.trabalho.grid(column=1, row=0, sticky=tk.NSEW)
        self.quadro.grid_columnconfigure(1, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.trabalho, background="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.coordenadas = tk.Label(self.trabalho, text="Mova o mouse")
        self.coordenadas.pack(ipadx=10, ipady=10)

    def cria_barra(self):
        self.barra = tk.Frame(self.quadro, width=100, height=600)
        self.blinha = ttk.Button(
            self.barra, text="Linha", padding="10", command=self.ferramenta_linha
        )
        self.blinha.pack()
        self.boval = ttk.Button(
            self.barra, text="Círculo", padding="10", command=self.ferramenta_oval
        )
        self.boval.pack()
        self.bretângulo = ttk.Button(
            self.barra,
            text="Retângulo",
            padding="10",
            command=self.ferramenta_retângulo,
        )
        self.bretângulo.pack()
        bdesfaz = ttk.Button(
            self.barra, text="Desfaz", padding="10", command=self.desfaz
        )
        bdesfaz.pack()
        blimpa = ttk.Button(self.barra, text="Limpa", padding="10", command=self.limpa)
        blimpa.pack()
        self.lfrente = ttk.Label(self.barra, text="Cor de Frente")
        self.lfrente.pack()
        self.bfrente = tk.Button(
            self.barra, text="Cor", command=self.cor_frente, bg=self.cor_de_frente
        )
        self.bfrente.pack(fill="x")
        self.lfundo = ttk.Label(self.barra, text="Cor de Fundo")
        self.lfundo.pack()
        self.bfundo = tk.Button(
            self.barra, text="Transparente", command=self.cor_fundo, bg=None
        )
        self.bfundo.pack(fill="x")
        self.bsalva = ttk.Button(
            self.barra, text="Salva", padding="10", command=self.salva
        )
        self.bsalva.pack(fill="x")
        self.bcarrega = ttk.Button(
            self.barra, text="Carrega", padding="10", command=self.carrega
        )
        self.bcarrega.pack(fill="x")
        self.barra.grid(column=0, row=0, sticky=tk.NS)

    def desfaz(self):
        if itens := self.canvas.find_withtag("desenho"):
            self.canvas.delete(itens[-1])

    def limpa(self):
        self.canvas.delete("desenho")

    def salva(self):
        nome = asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", ".json")]
        )
        if not nome:
            return  # Usuário cancelou
        desenho = {}  # Cria um dicionário com os objetos desenhados
        for item in self.canvas.find_withtag("desenho"):
            desenho[item] = {
                "tipo": (tipo := self.canvas.type(item)),
                "coordenadas": self.canvas.coords(item),
                "fill": self.canvas.itemcget(item, "fill"),
            }
            if tipo in ["rectangle", "oval"]:
                outline = self.canvas.itemcget(item, "outline")
                desenho[item]["outline"] = outline
        with open(nome, "w") as f:
            json.dump(desenho, f)

    def carrega(self):
        nome = askopenfilename(filetypes=[("JSON", ".json")])
        if not nome:
            return  # Usuário cancelou
        with open(nome, "r") as f:
            desenho = json.load(f)
        self.limpa()
        for dados in desenho.values():
            match dados["tipo"]:
                case "line":
                    self.canvas.create_line(
                        dados["coordenadas"], fill=dados["fill"], tags=["desenho"]
                    )
                case "rectangle":
                    self.canvas.create_rectangle(
                        dados["coordenadas"],
                        fill=dados["fill"],
                        outline=dados["outline"],
                        tags=["desenho"],
                    )
                case "oval":
                    self.canvas.create_oval(
                        dados["coordenadas"],
                        fill=dados["fill"],
                        outline=dados["outline"],
                        tags=["desenho"],
                    )

    def cor_fundo(self):
        cor = askcolor(title="Cor de fundo")
        self.cor_de_fundo = cor[1] or ""
        self.bfundo.config(
            text="Transparente" if self.cor_de_fundo == "" else "",
            background=self.cor_de_fundo or "SystemButtonFace",
        )

    def cor_frente(self):
        cor = askcolor(title="Cor de frente")
        if cor[1]:
            self.cor_de_frente = cor[1]
            self.bfrente.config(background=self.cor_de_frente)

    def ferramenta_linha(self):
        self.ferramenta = self.canvas.create_line

    def ferramenta_oval(self):
        self.ferramenta = self.canvas.create_oval

    def ferramenta_retângulo(self):
        self.ferramenta = self.canvas.create_rectangle

    def mouse_move(self, event):
        self.coordenadas["text"] = f"Mouse x={event.x} y ={event.y}"
        self.canvas.coords(
            self.cruz[0], event.x, 0, event.x, self.canvas.winfo_height()
        )
        self.canvas.coords(self.cruz[1], 0, event.y, self.canvas.winfo_width(), event.y)
        if self.estado == 1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_click(self, event):
        if self.estado == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.ferramenta(
                (self.xi, self.yi, event.x, event.y),
                fill=self.cor_de_frente,
                tags=["desenho"],
            )
            tipo = self.canvas.type(self.curr_id)
            if tipo in ["rectangle", "oval"]:
                self.canvas.itemconfig(
                    self.curr_id,
                    {
                        "outline": self.cor_de_frente,
                        "fill": self.cor_de_fundo,
                    },
                )
            self.estado = 1

    def mouse_release(self, event):
        if self.estado == 1:
            self.estado = 0


App().mainloop()
