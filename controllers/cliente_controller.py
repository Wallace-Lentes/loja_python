from database import conectar
from clientes import Clientes
import main
from datetime import datetime

def salvar_cliente(nome, cpf, email, telefone):
    conexao = conectar()
    cliente = Clientes(
        nome=nome,
        cpf=cpf,
        email=email,
        telefone=telefone,
        data_cadastro=datetime.now()
    )
    main.inserir_cliente(conexao, cliente)
    conexao.close()
