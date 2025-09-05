from database import conectar
from produtos import Produto
import main

def salvar_produto(nome, descricao, preco, estoque, id_categoria):
    conexao = conectar()
    produto = Produto(
        nome=nome,
        descricao=descricao,
        preco=float(preco),
        estoque=int(estoque),
        id_categoria=int(id_categoria)
    )
    main.inserir_produto(conexao, produto)
    conexao.close()
