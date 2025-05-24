import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        nome = input("Digite o nome do produto a alterar preço: ")
        cursor.execute(
            """select * from precos
            where nome = ?""",
            (nome,),
        )
        resultado = cursor.fetchone()
        if resultado:

            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            novo_preço = float(input("Digite o novo preço: "))
            cursor.execute(
                """update precos
                set preco = ?
                where nome = ?""",
                (novo_preço, nome),
            )
            print(f"O preço do produto {nome} foi alterado para {novo_preço:.2f}. ")
        else:
            print("Não encontrado.")
