from database import conectar
from pedidos import Pedido
from datetime import datetime

def salvar_pedido(id_cliente, valor_total=0, status="Pendente"):
    conexao = conectar()
    pedido = Pedido(id_cliente, valor_total, status, datetime.now())
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO pedido(id_cliente, data_pedido, valor_total, status)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (pedido.id_cliente, pedido.data_pedido, pedido.valor_total, pedido.status))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
