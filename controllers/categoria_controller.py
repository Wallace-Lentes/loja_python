from database import conectar
from categorias import Categoria

def salvar_categoria(nome, descricao):
    conexao = conectar()
    categoria = Categoria(nome, descricao)
    
    cursor = conexao.cursor()
    sql = "INSERT INTO categoria(nome, descricao) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (categoria.nome, categoria.descricao))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()
