from database import conectar
from produtos import Produto

def salvar_produto(nome, descricao, preco, estoque, id_categoria):
    conexao = conectar()
    produto = Produto(nome, descricao, preco, estoque, id_categoria)
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto(nome, descricao, preco, estoque, id_categoria)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.id_categoria))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
