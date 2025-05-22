import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        # cursor.execute(
        #     """update precos
        #                set preco = preco * 1.21"""
        # )

        # conexao.rollback()
        cursor.execute("""select * from precos""")
        for resultado in cursor.fetchall():
            print("Nome: {0:30s} Preço {1:6.2f}".format(*resultado))
