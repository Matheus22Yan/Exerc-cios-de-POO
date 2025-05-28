import re

codigo = "ABC431DEF901cC431203FXEW9"

# resultado = re.match("ABC", codigo) #INICIO DA STRING
resultado = re.search("DEF", codigo)  # QUALQUER POSICAO
resultado = re.findall("E", codigo)  # lista com todos padroes encontrados na string
resultado = re.findall(
    "E|F", codigo
)  # encontrar todos os caracteres E ou F na string usando a barra = |
resultado = re.findall("EF", codigo)  # sem a barra, somente E seguido de F
resultado = re.findall(
    "[ABF]", codigo
)  # especificando uma lista de caracteres que queremos encontrar
resultado = re.findall("[ABCDEFXW]", codigo)  # todas as letras
resultado = re.findall("[A-FXW]", codigo)  # forma abreviada
resultado = re.findall("[A-Z]", codigo)  # outra forma para vim todos
resultado = re.findall("[0-9]", codigo)  # mostrar todos os numeros
resultado = re.findall(
    "[A-Za-z]", codigo
)  # buscar tantas as letras maisculas como as minusculas
resultado = re.findall("[A-Za-z]", "avião")  # vem sem as letras acentuadas
resultado = re.findall(
    "\\d", codigo
)  # abreviações ou codigos especiais para achar um padrao(numericos)
resultado = re.findall(
    r"\d", codigo
)  # usando r para poder usar strings cruas que sejam diferentes de codigo de escape
resultado = re.findall(
    r"[\d]", codigo
)  # usando abreviações dentro da classe de caracteres
resultado = re.findall(r"[^\d]", codigo)  # incluir todos caracteres nao numericos
resultado = re.findall(r"[\D]", codigo)  # negando o padrao usando D maisculo
resultado = re.findall(r"\w", codigo)  # todos os caracteres alfabéticos, numéricos
resultado = re.findall(r"\w", "avião")  # inclui os caracteres acentuados tambem
resultado = re.findall(r"\W", "avião - 777")  # negada com W maisculo
resultado = re.findall(r"\w", "avião - 777")  # mostra tudo com w minusculo
resultado = re.findall(r"[^\W\d_]", "avião - 777_")  # apenas as letras, sem os números
resultado = re.findall(
    r"[\s]", "avião - 777"
)  # ver os vários caracteres em branco da string
resultado = re.findall(
    r"\d+", codigo
)  # para agrupar todos os caracteres, ao inves de ficarem apenas isolados
resultado = re.findall(
    r"\w+", codigo
)  # agrupar todos caracteres numericos e alfabeticos
resultado = re.findall(r"[^\W\d_]", codigo)  # todos as letras, sem os numeros
resultado = re.findall(
    r"\s*\d+", "1234"
)  # usar * para indicar zero ou mais vezes, deixando certas ocorrências serem opcionais
resultado = re.findall(r"\s*\d+", " 1234")  # zero ou mais espaços em branco no início
resultado = re.findall(r"\s*\d+", "  1234")  # zero ou mais espaços em branco no início
resultado = re.findall(
    r"\s*(\d+)", "  1234"
)  # se quisermos algumas partes do padrão encontrado no retorno, podemos criar um grupo, envolvendo a parte da expressão
resultado = re.findall(
    r"A?(\d+)", "1234"
)  # também podemos usar o ? para indicar um caractere opcional
resultado = re.findall(r"A?(\d+)", "A1234")  # outro exemplo
resultado = re.findall(r"\(\d+\)", "(92)9981-8912")  # exemplo do telefone do livro
resultado = re.findall(r"\(\d{2,3}\)", "(92)9981-8912")  # o mínimo e o máximo entre ()
resultado = re.findall(
    r"\(\d{2,3}\)", "(092)9981-8912"
)  # exemplo aplicado para testar o min e o max
resultado = re.findall(
    r"\(\d{2,3}\)", "(0921)9981-8912"
)  # volta nada, pois esta fora do padrao (min e max)
resultado = re.findall(r"\(\d{3}\)", "(92)9981-8912")  # so o minimo = 3
resultado = re.findall(r"\(\d{,3}\)", "(092)9981-8912")  # so o maximo = ,3
resultado = re.findall(
    r"\(\d{2,3}\)\d{4}-\d{4,5}", "(92)9981-8912"
)  # o (DDD) 4 DIGITOS -(TRACO) + 4 DIGITOS
# deixar o DDD opcional
resultado = re.match(r"(\(\d{2,3}\))?\d{4}-\d{4,5}", "(92)9981-8912")
resultado = re.match(r"(\(\d{2,3}\))?\d{4}-\d{4,5}", "9981-8912")
resultado = re.findall(
    r"(\(\d{2,3}\))?\d{4}-\d{4,5}", "   (92)9981-8912 "
)  # especificar o grupo do DDD como um grupo não capturado, ou seja, que existe na expressão regular, mas que não é retornado.
resultado = re.findall(r"(?:\(\d{2,3}\))?\s*\d{4}-\d{4,5}", "  (92) 9981-8912  ")

frase = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."

resultado = re.findall(
    r"(?:\(\d{2,3}\))?\s*\d{4}-\d{4,5}", frase
)  # retornar o telefone

# capturar os valores em reais/expressão que aceite o R$ seguido de espaços opcionais e de um número que pode ter ou não uma vírgula
resultado = re.findall(r"[Rr]\$\s*\d*,?\d*", frase)
resultado = re.findall(r"[Rr]\$\s*\d*,?\d*", "r$ 10002,1")
resultado = re.findall(r"[Rr]\$\s*\d*,?\d*", "R$ 12,12")
resultado = re.findall(
    r"[Rr]\$\s*(\d*,?\d*)", "R$ 12,12"
)  # usando um grupo, podemos extrair apenas o número
resultado = re.findall(
    r"r\$\s*(\d*,?\d*)", "R$ 12,12", re.IGNORECASE
)  # identificar padrões, desconsiderando as diferenças entre letras minúsculas e maiúsculas. Nesses casos, devemos passar a opção re. IGNORECASE
resultado = re.findall(
    r"(\w+).$", frase
)  # para retornarmos a última palavra ou número no fim da frase
resultado = re.findall(r"(\d{2}/\d{2}/\d{4})", frase)  # extrair as datas da frase

# capturar O texto escrito entre aspas de nossa string
exemplo = 'Olá mundo. Tudo "bem"? por "ai"?'
resultado = re.findall(r"\".*\"", exemplo)
# Se quisermos capturar os dois textos entre aspas
resultado = re.findall(r"\".*?\"", exemplo)

# casos em que repetiremos a pesquisa várias vezes, é mais interessante compilarmos a expressão. Dessa forma, ela será interpretada uma única vez e o resultado pode ser aplicado para realizar as operações mais rapidamente.
entre_aspas = re.compile(r"\".*?\"")
# print(entre_aspas.findall(exemplo))
print(entre_aspas.search(exemplo))

print(resultado)
