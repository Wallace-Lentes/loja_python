from database import conectar
from clientes import Clientes
from datetime import datetime

def salvar_cliente(nome, cpf, email, telefone):
    conexao = conectar()
    cliente = Clientes(nome, cpf, email, telefone, data_cadastro=datetime.now())
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO cliente(nome, cpf, email, telefone, data_cadastro)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (cliente.nome, cliente.cpf, cliente.email, cliente.telefone, cliente.data_cadastro))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
