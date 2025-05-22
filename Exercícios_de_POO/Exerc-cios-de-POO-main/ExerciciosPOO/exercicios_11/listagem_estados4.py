import sqlite3

print("Região Estados População  Mínima    Máxima      Média     Total (soma)")
print("====== ========         =========  =========  =========    ========== ")
conexao = sqlite3.connect("estado copy.db")
cursor = conexao.cursor()

# add having count(*)>5
# having count(*)>5
# order by tpop desc
for regiao in conexao.execute(
    """select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) as tpop 
        
                from estados                  
                group by regiao
                """
):
    print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*regiao))
print(
    "\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
        *conexao.execute(
            """select count(*),  min(populacao), max(populacao), avg(populacao), sum(populacao) from estados"""
        ).fetchone()
    )
)
