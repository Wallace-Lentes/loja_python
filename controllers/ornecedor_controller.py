from database import conectar
from fornecedores import Fornecedor

def salvar_fornecedor(nome, cnpj, telefone, email):
    conexao = conectar()
    fornecedor = Fornecedor(nome, cnpj, telefone, email)
    
    cursor = conexao.cursor()
    sql = """
        INSERT INTO fornecedor(nome, cnpj, telefone, email)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (fornecedor.nome, fornecedor.cnpj, fornecedor.telefone, fornecedor.email))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
