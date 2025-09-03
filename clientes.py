# clientes.py

from datetime import datetime

class Clientes:
    def __init__(self, nome, cpf, email, telefone, data_cadastro=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        # Se não passar data, usamos a data atual
        self.data_cadastro = data_cadastro if data_cadastro else datetime.now()
