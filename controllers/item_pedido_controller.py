from database import conectar
from itens_pedido import ItemPedido

def salvar_item_pedido(id_pedido, id_produto, quantidade, preco_unitario):
    conexao = conectar()
    item = ItemPedido(id_pedido, id_produto, quantidade, preco_unitario)
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO item_pedido(id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (item.id_pedido, item.id_produto, item.quantidade, item.preco_unitario))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
