import tkinter as tk
from tkinter import ttk, messagebox
from controllers import cliente_controller
from controllers import categoria_controller
from controllers import produto_controller
from controllers import pedido_controller



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Loja")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.eval('tk::PlaceWindow . center')

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

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

        def salvar():
            cliente_controller.salvar_cliente(nome.get(), cpf.get(), email.get(), telefone.get())
            messagebox.showinfo("Sucesso", "Cliente salvo!")

        tk.Button(self.clientes_tab, text="Salvar Cliente", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)

    # CATEGORIAS 
    def _categorias_form(self):
        tk.Label(self.categorias_tab, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.categorias_tab, text="Descrição").grid(row=1, column=0, padx=10, pady=5)

        nome = tk.Entry(self.categorias_tab); nome.grid(row=0, column=1)
        descricao = tk.Entry(self.categorias_tab); descricao.grid(row=1, column=1)

        def salvar():
            categoria_controller.salvar_categoria(nome.get(), descricao.get())
            messagebox.showinfo("Sucesso", "Categoria salva!")

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
            produto_controller.salvar_produto(nome.get(), descricao.get(), preco.get(), estoque.get(), id_categoria.get())
            messagebox.showinfo("Sucesso", "Produto salvo!")

        tk.Button(self.produtos_tab, text="Salvar Produto", command=salvar).grid(row=5, column=0, columnspan=2, pady=10)

    # PEDIDOS
    def _pedidos_form(self):
        tk.Label(self.pedidos_tab, text="ID Cliente").grid(row=0, column=0, padx=10, pady=5)

        id_cliente = tk.Entry(self.pedidos_tab); id_cliente.grid(row=0, column=1)

        def salvar():
            pedido_controller.salvar_pedido(id_cliente.get())
            messagebox.showinfo("Sucesso", "Pedido salvo!")

        tk.Button(self.pedidos_tab, text="Salvar Pedido", command=salvar).grid(row=1, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
