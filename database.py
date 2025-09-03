# db.py
import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="novaloja",
            user="postgres",
            password="123456"
        )
        print("Conectado ao PostgreSQL com sucesso!")
        return conexao
    except Exception as e:
        print("Erro ao conectar:", e)
        exit()
