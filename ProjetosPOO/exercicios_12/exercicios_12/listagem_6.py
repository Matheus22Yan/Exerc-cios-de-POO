import re

# reais = re.compile(r"r\$\s*\d+,?\d+", re.IGNORECASE)
# print(reais.match("R$ 10,20"))
# print(reais.match("R$ 10"))
# print(reais.match("R$ 132,"))

# reais = re.compile(r"r\$\s*(\d+),?(\d+)", re.IGNORECASE)
# valores = reais.match("R$ 100,99")
# print(valores.groups())

# reais = re.compile(
#     r"r\$\s*(?P<principal>\d+),?(?P<centavos>\d+)", re.IGNORECASE
# )  # ?P<nome> para nomear um grupo

# valores = reais.match("R$ 100,99")
# print(valores.groupdict())
# print(valores.group("principal"))
# print(valores.group("centavos"))
# print(valores.group(0))
# print(valores.group(1))
# print(valores.group(2))

seq = re.compile(r"(?P<seq>\w{3})(.*?)(?P=seq)")
print(seq.match("AAAabcdefAAA").groups())
print(seq.match("AAAabcdefAAA").groupdict())

seq = re.compile(r"(\w{3})(.*?)(\1)")
print(seq.match("AAAabcdefAAA").groups())
