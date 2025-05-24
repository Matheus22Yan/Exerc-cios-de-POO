import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz. title("Primeira Janela")
raiz. geometry("250x50")
quadro = ttk.Frame(raiz)
texto = ttk.Label(quadro, text="Olá GUI!") 
texto.pack()

botão = ttk.Button(quadro, text="Sai", command=raiz. destroy)
botão.pack()
quadro.pack(expand=True)
raiz.mainloop()