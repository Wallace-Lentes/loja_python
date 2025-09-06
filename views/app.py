import tkinter as tk
from tkinter import ttk, messagebox

from controllers import (
    cliente_controller,
    categoria_controller,
    produto_controller,
    pedido_controller,
    item_pedido_controller,
    fornecedor_controller,
    produto_fornecedor_controller
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Loja")
        self.geometry("800x600")
        self.configure(bg="#c51f1f")

        self.eval('tk::PlaceWindow . center')

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        self.clientes_tab = ttk.Frame(notebook)
        self.categorias_tab = ttk.Frame(notebook)
        self.produtos_tab = ttk.Frame(notebook)
        self.pedidos_tab = ttk.Frame(notebook)
        self.itens_tab = ttk.Frame(notebook)
        self.fornecedores_tab = ttk.Frame(notebook)
        self.produto_fornecedor_tab = ttk.Frame(notebook)

        notebook.add(self.clientes_tab, text="Clientes")
        notebook.add(self.categorias_tab, text="Categorias")
        notebook.add(self.produtos_tab, text="Produtos")
        notebook.add(self.pedidos_tab, text="Pedidos")
        notebook.add(self.itens_tab, text="Itens Pedido")
        notebook.add(self.fornecedores_tab, text="Fornecedores")
        notebook.add(self.produto_fornecedor_tab, text="Produto-Fornecedor")

        # Formularios
        self._clientes_form()
        self._categorias_form()
        self._produtos_form()
        self._pedidos_form()
        self._itens_form()
        self._fornecedores_form()
        self._produto_fornecedor_form()

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

        def salvar():
            try:
                cliente_controller.salvar_cliente(nome.get(), cpf.get(), email.get(), telefone.get())
                messagebox.showinfo("Sucesso", "Cliente salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.clientes_tab, text="Salvar Cliente", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)

    # CATEGORIAS
    def _categorias_form(self):
        tk.Label(self.categorias_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.categorias_tab, text="Descrição").grid(row=1, column=0, padx=10, pady=5)

        nome = tk.Entry(self.categorias_tab); nome.grid(row=0, column=1)
        descricao = tk.Entry(self.categorias_tab); descricao.grid(row=1, column=1)

        def salvar():
            try:
                categoria_controller.salvar_categoria(nome.get(), descricao.get())
                messagebox.showinfo("Sucesso", "Categoria salva!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.categorias_tab, text="Salvar Categoria", command=salvar).grid(row=2, column=0, columnspan=2, pady=10)

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

        def salvar():
            try:
                produto_controller.salvar_produto(nome.get(), descricao.get(), float(preco.get()), int(estoque.get()), id_categoria.get())
                messagebox.showinfo("Sucesso", "Produto salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.produtos_tab, text="Salvar Produto", command=salvar).grid(row=5, column=0, columnspan=2, pady=10)

    # PEDIDO
    def _pedidos_form(self):
        tk.Label(self.pedidos_tab, text="ID Cliente").grid(row=0, column=0, padx=10, pady=5)
        id_cliente = tk.Entry(self.pedidos_tab); id_cliente.grid(row=0, column=1)

        def salvar():
            try:
                pedido_controller.salvar_pedido(int(id_cliente.get()))
                messagebox.showinfo("Sucesso", "Pedido salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.pedidos_tab, text="Salvar Pedido", command=salvar).grid(row=1, column=0, columnspan=2, pady=10)

    # ITENS PEDIDO 
    def _itens_form(self):
        tk.Label(self.itens_tab, text="ID Pedido").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.itens_tab, text="ID Produto").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.itens_tab, text="Quantidade").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.itens_tab, text="Preço Unitário").grid(row=3, column=0, padx=10, pady=5)

        id_pedido = tk.Entry(self.itens_tab); id_pedido.grid(row=0, column=1)
        id_produto = tk.Entry(self.itens_tab); id_produto.grid(row=1, column=1)
        quantidade = tk.Entry(self.itens_tab); quantidade.grid(row=2, column=1)
        preco_unitario = tk.Entry(self.itens_tab); preco_unitario.grid(row=3, column=1)

        def salvar():
            try:
                item_pedido_controller.salvar_item_pedido(
                    int(id_pedido.get()), int(id_produto.get()), int(quantidade.get()), float(preco_unitario.get())
                )
                messagebox.showinfo("Sucesso", "Item de pedido salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.itens_tab, text="Salvar Item", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)

    # FORNECEDOR
    def _fornecedores_form(self):
        tk.Label(self.fornecedores_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.fornecedores_tab, text="CNPJ").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.fornecedores_tab, text="Telefone").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.fornecedores_tab, text="Email").grid(row=3, column=0, padx=10, pady=5)

        nome = tk.Entry(self.fornecedores_tab); nome.grid(row=0, column=1)
        cnpj = tk.Entry(self.fornecedores_tab); cnpj.grid(row=1, column=1)
        telefone = tk.Entry(self.fornecedores_tab); telefone.grid(row=2, column=1)
        email = tk.Entry(self.fornecedores_tab); email.grid(row=3, column=1)

        def salvar():
            try:
                fornecedor_controller.salvar_fornecedor(nome.get(), cnpj.get(), telefone.get(), email.get())
                messagebox.showinfo("Sucesso", "Fornecedor salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.fornecedores_tab, text="Salvar Fornecedor", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)

    # PRODUTO FORNECEDOR
    def _produto_fornecedor_form(self):
        tk.Label(self.produto_fornecedor_tab, text="ID Produto").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.produto_fornecedor_tab, text="ID Fornecedor").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.produto_fornecedor_tab, text="Preço de Compra").grid(row=2, column=0, padx=10, pady=5)

        id_produto = tk.Entry(self.produto_fornecedor_tab); id_produto.grid(row=0, column=1)
        id_fornecedor = tk.Entry(self.produto_fornecedor_tab); id_fornecedor.grid(row=1, column=1)
        preco_compra = tk.Entry(self.produto_fornecedor_tab); preco_compra.grid(row=2, column=1)

        def salvar():
            try:
                produto_fornecedor_controller.salvar_produto_fornecedor(
                    int(id_produto.get()), int(id_fornecedor.get()), float(preco_compra.get())
                )
                messagebox.showinfo("Sucesso", "Produto-Fornecedor salvo!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(self.produto_fornecedor_tab, text="Salvar Produto-Fornecedor", command=salvar).grid(row=3, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
