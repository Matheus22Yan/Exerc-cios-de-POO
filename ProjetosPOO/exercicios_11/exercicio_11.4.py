import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        preço1 = float(input("Digite o menor preço a listar: "))
        preço2 = float(input("Digite o maior preço a listar: "))
        cursor.execute(
            """select * from precos
            where preco >= ? and preco <= ?""",
            (preço1, preço2),
        )
        achados = 0
        for resultado in cursor.fetchall():
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            achados += 1
        if achados == 0:
            print("Não encontrado.")
        else:
            print("{} produto(s) encontrado(s).".format(achados))
