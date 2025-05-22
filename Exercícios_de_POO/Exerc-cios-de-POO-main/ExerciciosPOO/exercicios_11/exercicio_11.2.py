import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:

        # cursor.execute(
        #     """
        #     create table precos(
        #     nome text,
        #     preco numeric)
        # """
        # )
        cursor.execute("delete from precos")
        cursor.executemany(
            """
            insert into precos (nome, preco)
            values(?, ?)
            """,
            [
                ("Batata", "3.20"),
                ("Pão", "1.20"),
                ("Mamão", "2.14"),
            ],
        )
        # cursor.execute("select * from precos")

        # resultado = cursor.fetchall()
        # for nome, preco in resultado:
        #     print(f"Nome: {nome}\nPreço: {preco}")

        cursor.execute("""select * from precos""")
        resultado = cursor.fetchall()
        for nome, preco in resultado:
            print(f"Nome: {nome}\n Preço: {preco}\n")

            # outra forma:
        # for resultado in cursor.fetchall():
        # print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))

cursor.close()
conexao.close()
