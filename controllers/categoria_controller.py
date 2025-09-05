from database import conectar
from categorias import Categoria
import main

def salvar_categoria(nome, descricao):
    conexao = conectar()
    categoria = Categoria(nome=nome, descricao=descricao)
    main.inserir_categoria(conexao, categoria)
    conexao.close()
