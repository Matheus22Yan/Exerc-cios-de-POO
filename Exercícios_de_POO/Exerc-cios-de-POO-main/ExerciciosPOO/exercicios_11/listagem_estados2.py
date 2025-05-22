import sqlite3

conexão = sqlite3.connect("estado copy.db")
conexão.row_factory = sqlite3.Row
print("%3s %-20s %12s" % ("id", "nome", "populacao"))
print("=" * 37)


for estado in conexão.execute("select * from estados order by populacao desc"):
    print("%3d %-20s %12d" % (estado["id"], estado["nome"], estado["populacao"]))

conexão.close()
