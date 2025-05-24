import sqlite3
from contextlib import closing

with sqlite3.connect("estado copy.db") as conexao:
    with closing(conexao.cursor()) as cursor:

        try:
            cursor.execute("ALTER TABLE estados ADD COLUMN sigla TEXT")
        except sqlite3.OperationalError:
            pass  # A coluna já existe

        try:
            cursor.execute("ALTER TABLE estados ADD COLUMN regiao TEXT")
        except sqlite3.OperationalError:
            pass  # A coluna já existe

        dados = [
            ["SP", "SE", "São Paulo"],
            ["MG", "SE", "Minas Gerais"],
            ["RJ", "SE", "Rio de Janeiro"],
            ["BA", "NE", "Bahia"],
            ["RS", "S", "Rio Grande do Sul"],
            ["PR", "S", "Paraná"],
            ["PE", "NE", "Pernambuco"],
            ["CE", "NE", "Ceará"],
            ["PA", "N", "Pará"],
            ["MA", "NE", "Maranhão"],
            ["SC", "S", "Santa Catarina"],
            ["GO", "CO", "Goiás"],
            ["PB", "NE", "Paraíba"],
            ["ES", "SE", "Espírito Santo"],
            ["AM", "N", "Amazonas"],
            ["RN", "NE", "Rio Grande do Norte"],
            ["AL", "NE", "Alagoas"],
            ["PI", "NE", "Piauí"],
            ["MT", "CO", "Mato Grosso"],
            ["DF", "CO", "Distrito Federal"],
            ["MS", "CO", "Mato Grosso do Sul"],
            ["SE", "NE", "Sergipe"],
            ["RO", "N", "Rondônia"],
            ["TO", "N", "Tocantins"],
            ["AC", "N", "Acre"],
            ["AP", "N", "Amapá"],
            ["RR", "N", "Roraima"],
        ]
        for sigla, regiao, nome in dados:
            cursor.execute(
                """update estados
                        set sigla = ?,
                        regiao = ? 
                        where nome = ?""",
                (sigla, regiao, nome),
            )
        cursor.execute("select * from estados")
        print("Dados após o UPDATE:")
        for row in cursor.fetchall():
            print(row)
