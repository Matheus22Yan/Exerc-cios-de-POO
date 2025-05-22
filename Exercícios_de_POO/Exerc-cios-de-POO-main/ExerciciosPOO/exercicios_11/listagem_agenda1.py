import sqlite3

conexao = sqlite3.connect("agenda copy.db")
cursor = conexao.cursor()


cursor.execute("Drop table if exists agenda")

cursor.execute(
    """create table agenda(
    id integer primary key autoincrement,
    nome text,
    telefone text
    )"""
)

dados = [
    ["André", "33324 - 2222"],
    ["Matheus", "33324 - 2222"],
    ["Diogo", "33324 - 2222"],
    ["Bahia", "33324 - 2222"],
]

cursor.executemany("insert into agenda(nome, telefone) values(?, ?)", dados)

cursor.execute("select * from agenda")
print(f"Registros atuais na tabela {'agenda'}:")
for id, nome, telefone in cursor.fetchall():
    print(f"ID: {id}, Nome: {nome}, Telefone: {telefone}")


conexao.commit()
cursor.close()
conexao.close()
