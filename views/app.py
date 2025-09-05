import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar
from clientes import Clientes
from categorias import Categoria
from produtos import Produto
from pedidos import Pedido
from datetime import datetime
import main  # importa as funções de inserção


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Loja")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.eval('tk::PlaceWindow . center')

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        # Abas
        self.clientes_tab = ttk.Frame(notebook)
        self.categorias_tab = ttk.Frame(notebook)
        self.produtos_tab = ttk.Frame(notebook)
        self.pedidos_tab = ttk.Frame(notebook)

        notebook.add(self.clientes_tab, text="Clientes")
        notebook.add(self.categorias_tab, text="Categorias")
        notebook.add(self.produtos_tab, text="Produtos")
        notebook.add(self.pedidos_tab, text="Pedidos")

        # formulários
        self._clientes_form()
        self._categorias_form()
        self._produtos_form()
        self._pedidos_form()

    # CLIENTES
    def _clientes_form(self):
        tk.Label(self.clientes_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.clientes_tab, text="CPF").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.clientes_tab, text="Email").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.clientes_tab, text="Telefone").grid(row=3, column=0, padx=10, pady=5)

        nome = tk.Entry(self.clientes_tab); nome.grid(row=0, column=1)
        cpf = tk.Entry(self.clientes_tab); cpf.grid(row=1, column=1)
        email = tk.Entry(self.clientes_tab); email.grid(row=2, column=1)
        telefone = tk.Entry(self.clientes_tab); telefone.grid(row=3, column=1)

        def salvar_cliente():
            conexao = conectar()
            cliente = Clientes(
                nome=nome.get(),
                cpf=cpf.get(),
                email=email.get(),
                telefone=telefone.get(),
                data_cadastro=datetime.now()
            )
            main.inserir_cliente(conexao, cliente)
            conexao.close()
            messagebox.showinfo("Sucesso", "Cliente salvo!")

        tk.Button(self.clientes_tab, text="Salvar Cliente", command=salvar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

    # FORM CATEGORIAS
    def _categorias_form(self):
        tk.Label(self.categorias_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.categorias_tab, text="Descrição").grid(row=1, column=0, padx=10, pady=5)

        nome = tk.Entry(self.categorias_tab); nome.grid(row=0, column=1)
        descricao = tk.Entry(self.categorias_tab); descricao.grid(row=1, column=1)

        def salvar_categoria():
            conexao = conectar()
            categoria = Categoria(nome=nome.get(), descricao=descricao.get())
            main.inserir_categoria(conexao, categoria)
            conexao.close()
            messagebox.showinfo("Sucesso", "Categoria salva!")

        tk.Button(self.categorias_tab, text="Salvar Categoria", command=salvar_categoria).grid(row=2, column=0, columnspan=2, pady=10)

    # PRODUTOS
    def _produtos_form(self):
        tk.Label(self.produtos_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.produtos_tab, text="Descrição").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.produtos_tab, text="Preço").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.produtos_tab, text="Estoque").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self.produtos_tab, text="ID Categoria").grid(row=4, column=0, padx=10, pady=5)

        nome = tk.Entry(self.produtos_tab); nome.grid(row=0, column=1)
        descricao = tk.Entry(self.produtos_tab); descricao.grid(row=1, column=1)
        preco = tk.Entry(self.produtos_tab); preco.grid(row=2, column=1)
        estoque = tk.Entry(self.produtos_tab); estoque.grid(row=3, column=1)
        id_categoria = tk.Entry(self.produtos_tab); id_categoria.grid(row=4, column=1)

        def salvar_produto():
            conexao = conectar()
            produto = Produto(
                nome=nome.get(),
                descricao=descricao.get(),
                preco=float(preco.get()),
                estoque=int(estoque.get()),
                id_categoria=int(id_categoria.get())
            )
            main.inserir_produto(conexao, produto)
            conexao.close()
            messagebox.showinfo("Sucesso", "Produto salvo!")

        tk.Button(self.produtos_tab, text="Salvar Produto", command=salvar_produto).grid(row=5, column=0, columnspan=2, pady=10)

    # PEDIDOS 
    def _pedidos_form(self):
        tk.Label(self.pedidos_tab, text="ID Cliente").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.pedidos_tab, text="Data").grid(row=1, column=0, padx=10, pady=5)

        id_cliente = tk.Entry(self.pedidos_tab); id_cliente.grid(row=0, column=1)
        data = tk.Entry(self.pedidos_tab); data.grid(row=1, column=1)

        def salvar_pedido():
            conexao = conectar()
            pedido = Pedido(id_cliente=int(id_cliente.get()), data=datetime.now())
            main.inserir_pedido(conexao, pedido)
            conexao.close()
            messagebox.showinfo("Sucesso", "Pedido salvo!")

        tk.Button(self.pedidos_tab, text="Salvar Pedido", command=salvar_pedido).grid(row=2, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
