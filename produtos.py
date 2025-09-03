class Produto:
    def __init__(self, nome, descricao, preco, estoque, id_categoria=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria
