import sqlite3
import datetime


def adptador_data(val):
    return val.isoformat()


def converter_data(val):
    return datetime.date.fromisoformat(val.decode("utf-8"))


hoje = datetime.date.today()
hoje30dias = hoje + datetime.timedelta(days=30)

sqlite3.register_adapter(datetime.date, adptador_data)
sqlite3.register_converter("DATE", converter_data)

conexao = sqlite3.connect("data.db", detect_types=sqlite3.PARSE_DECLTYPES)
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("Drop table if exists feriados")

cursor.execute(
    """create table feriados(
            id integer primary key autoincrement,
            data date unique,
            descricao text)"""
)

feriados = [
    ["2025-05-20", "Feriado Próximo 1"],
    ["2025-06-10", "Feriado no Meio"],
    ["2025-07-10", "Feriado Quase no Fim"],
    ["2025-04-21", "Tiradentes"],
    ["2025-05-01", "Dia do trabalhador"],
    ["2025-09-07", "Independência"],
    ["2025-10-12", "Padroeira do Brasil"],
    ["2025-11-02", "Finados"],
    ["2025-08-15", "Feriado Depois (Fora)"],
    ["2025-11-15", "Proclamação da República"],
    ["2025-12-25", "Natal"],
]

cursor.executemany("insert into feriados(data, descricao) values (?,?)", feriados)


for feriado in conexao.execute(
    "select * from feriados where data >= ? and data <= ?", (hoje, hoje30dias)
):
    # print("{0} {1}".format(feriado["data"].strftime("%d/%m"), feriado["descricao"]))
    print(f"{feriado['data']:%d/%m} {feriado['descricao']}")
