import sqlite3
from contextlib import closing

conexao = sqlite3.connect("agenda copy.db")
cursor = conexao.cursor()

cursor.execute("select * from agenda")
print(f"Registros atuais na tabela {'agenda'}:")
for id, nome, telefone in cursor.fetchall():
    print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}")

cursor.execute(
    """delete from agenda
                where nome = 'André' """
)

print("Registros apagados : ", cursor.rowcount)
if cursor.rowcount > 0:
    conexao.commit()
    print("Alterações feitas")
else:
    conexao.rollback()
    print("Alterações abortadas")

cursor.execute("select * from agenda")
print(f"Registros atuais na tabela {'agenda'} após a exclusão:")
for id, nome, telefone in cursor.fetchall():
    print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}")

cursor.execute(
    "INSERT INTO agenda (nome, telefone) VALUES (?, ?)",
    ("André", "33324 - 2222"),
)
conexao.commit()
print("André inserido novamente.")

cursor.execute("select * from agenda")
print(f"Registros atuais na tabela {'agenda'} após reinserção:")
for id, nome, telefone in cursor.fetchall():
    print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}")

conexao.close()
