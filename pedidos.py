from datetime import datetime

class Pedido:
    def __init__(self, id_cliente, valor_total, status, data_pedido=None):
        self.id_cliente = id_cliente
        self.valor_total = valor_total
        self.status = status
        self.data_pedido = data_pedido or datetime.now()
