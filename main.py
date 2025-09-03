from database import conectar
from clientes import Clientes
from categorias import Categoria
from produtos import Produto
from pedidos import Pedido
from itens_pedido import ItemPedido
from fornecedores import Fornecedor
from produto_fornecedor import ProdutoFornecedor
from datetime import datetime


def inserir_cliente(conexao, cliente):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO cliente(nome, cpf, email, telefone, data_cadastro)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            cliente.nome,
            cliente.cpf,
            cliente.email,
            cliente.telefone,
            cliente.data_cadastro
        ))
        conexao.commit()
        print("Cliente inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_categoria(conexao, categoria):
    cursor = conexao.cursor()
    sql = "INSERT INTO categoria(nome, descricao) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (categoria.nome, categoria.descricao))
        conexao.commit()
        print("Categoria inserida com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir categoria:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_produto(conexao, produto):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto(nome, descricao, preco, estoque, id_categoria)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            produto.nome,
            produto.descricao,
            produto.preco,
            produto.estoque,
            produto.id_categoria
        ))
        conexao.commit()
        print("Produto inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir produto:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_pedido(conexao, pedido):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO pedido(id_cliente, data_pedido, valor_total, status)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            pedido.id_cliente,
            pedido.data_pedido,
            pedido.valor_total,
            pedido.status
        ))
        conexao.commit()
        print("Pedido inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir pedido:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_item_pedido(conexao, item):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO item_pedido(id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            item.id_pedido,
            item.id_produto,
            item.quantidade,
            item.preco_unitario
        ))
        conexao.commit()
        print("Item de pedido inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir item de pedido:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_fornecedor(conexao, fornecedor):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO fornecedor(nome, cnpj, telefone, email)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            fornecedor.nome,
            fornecedor.cnpj,
            fornecedor.telefone,
            fornecedor.email
        ))
        conexao.commit()
        print("Fornecedor inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir fornecedor:", e)
        conexao.rollback()
    finally:
        cursor.close()


def inserir_produto_fornecedor(conexao, pf):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto_fornecedor(id_produto, id_fornecedor, preco_compra)
        VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            pf.id_produto,
            pf.id_fornecedor,
            pf.preco_compra
        ))
        conexao.commit()
        print("Produto_Fornecedor inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir produto_fornecedor:", e)
        conexao.rollback()
    finally:
        cursor.close()


# MENU 
def main():
    conexao = conectar()

    while True:
        print("\n📌 MENU DE INSERÇÃO")
        print("1 - Inserir Cliente")
        print("2 - Inserir Categoria")
        print("3 - Inserir Produto")
        print("4 - Inserir Pedido")
        print("5 - Inserir Item de Pedido")
        print("6 - Inserir Fornecedor")
        print("7 - Inserir Produto_Fornecedor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cliente = Clientes(nome, cpf, email, telefone)
            inserir_cliente(conexao, cliente)

        elif opcao == "2":
            nome = input("Nome da categoria: ")
            descricao = input("Descrição: ")
            categoria = Categoria(nome, descricao)
            inserir_categoria(conexao, categoria)

        elif opcao == "3":
            nome = input("Nome do produto: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            id_categoria = input("ID da categoria (ou deixe vazio): ") or None
            produto = Produto(nome, descricao, preco, estoque, id_categoria)
            inserir_produto(conexao, produto)

        elif opcao == "4":
            id_cliente = int(input("ID do cliente: "))
            valor_total = float(input("Valor total: "))
            status = input("Status do pedido: ")
            pedido = Pedido(id_cliente, valor_total, status, datetime.now())
            inserir_pedido(conexao, pedido)

        elif opcao == "5":
            id_pedido = int(input("ID do pedido: "))
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            preco_unitario = float(input("Preço unitário: "))
            item = ItemPedido(id_pedido, id_produto, quantidade, preco_unitario)
            inserir_item_pedido(conexao, item)

        elif opcao == "6":
            nome = input("Nome do fornecedor: ")
            cnpj = input("CNPJ: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            fornecedor = Fornecedor(nome, cnpj, telefone, email)
            inserir_fornecedor(conexao, fornecedor)

        elif opcao == "7":
            id_produto = int(input("ID do produto: "))
            id_fornecedor = int(input("ID do fornecedor: "))
            preco_compra = float(input("Preço de compra: "))
            pf = ProdutoFornecedor(id_produto, id_fornecedor, preco_compra)
            inserir_produto_fornecedor(conexao, pf)

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("⚠️ Opção inválida!")

    conexao.close()


if __name__ == "__main__":
    main()
