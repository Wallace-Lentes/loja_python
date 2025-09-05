from database import conectar
from pedidos import Pedido
import main
from datetime import datetime

def salvar_pedido(id_cliente):
    conexao = conectar()
    pedido = Pedido(id_cliente=int(id_cliente), data=datetime.now())
    main.inserir_pedido(conexao, pedido)
    conexao.close()
