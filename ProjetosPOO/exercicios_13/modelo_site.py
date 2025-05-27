from uuid import uuid4
from datetime import date


class Site:
    def __init__(self, /, url=None, categoria=None, data=None, id=None, notas=None):
        if id is None:
            id = str(uuid4())
        self.id = id
        if data is None:
            data = date.today().strftime("%d-%m-%y")
        self.data = data
        self.url = url
        self.categoria = categoria
        self.notas = notas

    def __str__(self):
        return f"Site {self.id} {self.url} {self.categoria} {self.notas}"
