from database import conectar
from produto_fornecedor import ProdutoFornecedor

def salvar_produto_fornecedor(id_produto, id_fornecedor, preco_compra):
    conexao = conectar()
    pf = ProdutoFornecedor(id_produto, id_fornecedor, preco_compra)
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto_fornecedor(id_produto, id_fornecedor, preco_compra)
        VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(sql, (pf.id_produto, pf.id_fornecedor, pf.preco_compra))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
