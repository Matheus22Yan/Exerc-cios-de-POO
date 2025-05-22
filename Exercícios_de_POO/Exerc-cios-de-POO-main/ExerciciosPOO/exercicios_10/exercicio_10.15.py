from collections import UserList


class ListaUnica(UserList):
    def __init__(self, elem_classe, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_classe

    def append(self, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().append(elem)

    def extend(self, iteravel):
        for elem in iteravel:
            self.append(elem)

    def __setitem__(self, posicao, elem):
        self.verifica_tipo(elem)
        if elem not in self.data:
            super().__setitem__(posicao, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("Tipo inválido")


# Criando uma classe Produto para usar com ListaUnica
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco})"


# Exemplo de uso:
p1 = Produto("Camiseta", 30.0)
p2 = Produto("Calça", 80.0)
p3 = Produto("Camiseta", 30.0)  # Mesmo conteúdo de p1, mas outro objeto

estoque = ListaUnica(Produto)

estoque.append(p1)
estoque.append(p2)
estoque.append(p1)  # Ignorado (mesmo objeto)
estoque.append(p3)  # Adicionado (é outro objeto, mesmo conteúdo)

for produto in estoque:
    print(produto)
