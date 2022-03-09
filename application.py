import tkinter.messagebox
from datetime import date, datetime
from tkinter.font import BOLD
from tkinter.messagebox import *

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from constantes.directory_paths import *
from data_manager import DataManager


class Application(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.data_manager = DataManager()

        self.header = Header(
            master=self,
            bootstyle=SECONDARY
        )
        self.header.pack(side=TOP)

        self.body = Body(
            master=self,
            data_manager=self.data_manager,
            padding=20,
            height=600
        )
        self.body.pack(
            side=BOTTOM,
            fill=BOTH,
            expand=True
        )
        self.body.pack_propagate(False)


class Header(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.banner = Banner(
            master=self,
            padding=20,
            bootstyle=SECONDARY
        )
        self.banner.pack(
            side=TOP,
            fill=X,
            expand=True
        )

        self.menu_bar = MenuBar(
            master=self
        )
        self.menu_bar.pack(
            side=BOTTOM,
            fill=X,
            expand=True
        )


class Banner(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.images = [
            ttk.PhotoImage(
                name="logo",
                file=IMAGENS_PATH + "erp_64px.png")
        ]

        self.header_label = ttk.Label(
            master=self,
            image="logo",
            style=(INVERSE, SECONDARY)
        )
        self.header_label.pack(side=LEFT)

        self.header_label_2 = ttk.Label(
            master=self,
            text="Gerenciador de Estoque - Alunos: Marcos e Pablo",
            font=('TkDefaultFixed', 26),
            style=(INVERSE, SECONDARY)
        )
        self.header_label_2.pack(side=LEFT, padx=10)


class MenuBar(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.images = [
            ttk.PhotoImage(
                name="estoque",
                file=IMAGENS_PATH + "boxes_24px.png"),
            ttk.PhotoImage(
                name="vendas",
                file=IMAGENS_PATH + "cofrinho_24px.png"),
            ttk.PhotoImage(
                name="configurações",
                file=IMAGENS_PATH + "settings_24px.png"),
            ttk.PhotoImage(
                name="compras",
                file=IMAGENS_PATH + "shopping-cart_24px.png")
        ]

        self.btn_width = 150
        self.btn_height = 7

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="estoque",
            text="Estoque",
            compound=LEFT,
            bootstyle=INFO,
            command=self.estoque_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT,
            fill=BOTH,
            ipadx=self.btn_width,
            ipady=self.btn_height
        )

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="compras",
            text="Compras & Vendas",
            compound=LEFT,
            bootstyle=INFO,
            command=self.compras_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT,
            fill=BOTH,
            ipadx=self.btn_width,
            ipady=self.btn_height
        )

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="configurações",
            text="Cadastro",
            compound=LEFT,
            bootstyle=INFO,
            command=self.cadastro_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT,
            fill=BOTH,
            ipadx=self.btn_width,
            ipady=self.btn_height
        )

    def estoque_btn(self):
        body_instance = self.get_body_instance()
        body_instance.init_estoque()
        print("Clicou no Estoque.")

    def compras_btn(self):
        body_instance = self.get_body_instance()
        body_instance.init_compras_vendas()
        print("Clicou nas Compras & Vendas.")

    def cadastro_btn(self):
        body_instance = self.get_body_instance()
        body_instance.init_cadastro()
        print("Clicou no Cadastro.")

    def get_body_instance(self):
        main_instance = self
        while not isinstance(main_instance, Application):
            main_instance = main_instance.master
        for instance in main_instance.winfo_children():
            if isinstance(instance, Body):
                return instance


class Body(ttk.Frame):
    def __init__(self, data_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.init_cadastro()

    def destroy_widget_children(self):
        for children in self.winfo_children():
            children.destroy()

    def init_estoque(self):
        self.destroy_widget_children()
        Estoque(
            master=self,
            data_manager=self.data_manager
        ).pack(
            fill=BOTH,
            expand=True
        )

    def init_compras_vendas(self):
        self.destroy_widget_children()
        ComprasVendas(
            master=self,
            data_manager=self.data_manager
        ).pack(
            fill=BOTH,
            expand=True
        )

    def init_cadastro(self):
        self.destroy_widget_children()
        Cadastro(
            master=self,
            data_manager=self.data_manager
        ).pack(
            fill=BOTH,
            expand=True
        )


class Estoque(ttk.Frame):
    def __init__(self, data_manager=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.tree = ttk.Treeview(
            master=self,
            style=INFO
        )
        self.tree['columns'] = ("id", "produto", "fornecedor", "preco_compra", "preco_venda", "qtd", "data", "tempo")
        self.tree.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree.column("id", anchor=CENTER, width=20, minwidth=0)
        self.tree.column("produto", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("fornecedor", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("preco_compra", anchor=CENTER, width=-0, minwidth=0, stretch=NO)
        self.tree.column("preco_venda", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree.column("qtd", anchor=CENTER, width=40, minwidth=0)
        self.tree.column("data", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("tempo", anchor=CENTER, width=80, minwidth=0)
        self.tree.heading("#0", text="Label")
        self.tree.heading("id", text="ID")
        self.tree.heading("produto", text="Produto")
        self.tree.heading("fornecedor", text="Fornecedor")
        self.tree.heading("preco_compra", text="Preço de compra")
        self.tree.heading("preco_venda", text="Preço de venda")
        self.tree.heading("qtd", text="Quant.")
        self.tree.heading("data", text="Data")
        self.tree.heading("tempo", text="Hora")
        self.tree.pack(padx=30, pady=30, fill=BOTH, expand=YES)
        self.update_tree()

    def update_tree(self):
        self.clean_tree()
        registros: list = self.data_manager.get_estoque()
        for row in registros:
            self.tree.insert(
                parent='',
                index=END,
                iid=(str(row[0]) + ' ' + str(row[1])),
                values=row
            )

    def clean_tree(self):
        self.tree.delete(*self.tree.get_children())


class ComprasVendas(ttk.Frame):
    def __init__(self, data_manager=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.cadastro_compras = CadastroCompras(
            master=self,
            data_manager=self.data_manager
        )
        self.cadastro_compras.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        self.cadastro_vendas = CadastroVendas(
            master=self,
            data_manager=self.data_manager
        )
        self.cadastro_vendas.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )


class CadastroCompras(ttk.Frame):
    def __init__(self, data_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.tree = ttk.Treeview(
            master=self,
            style=INFO
        )
        self.tree['columns'] = ("id", "produto", "fornecedor", "preco_compra", "qtd", "data", "tempo")
        self.tree.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree.column("id", anchor=CENTER, width=20, minwidth=0)
        self.tree.column("produto", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("fornecedor", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("preco_compra", anchor=CENTER, width=40, minwidth=0)
        self.tree.column("qtd", anchor=CENTER, width=40, minwidth=0)
        self.tree.column("data", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("tempo", anchor=CENTER, width=80, minwidth=0)
        self.tree.heading("#0", text="Label")
        self.tree.heading("id", text="ID")
        self.tree.heading("produto", text="Produto")
        self.tree.heading("fornecedor", text="Fornecedor")
        self.tree.heading("preco_compra", text="Preço")
        self.tree.heading("qtd", text="Quant.")
        self.tree.heading("data", text="Data")
        self.tree.heading("tempo", text="Hora")
        self.tree.pack(padx=30, pady=5, fill=BOTH, expand=YES)
        self.update_tree()

        self.lbl_title = ttk.Label(
            self,
            text=f"REGISTRAR COMPRAS",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack(pady=5)

        self.lista_produtos: list = self.data_manager.get_nome_produtos()
        self.lista_produtos = list(set(self.lista_produtos))

        self.combobox_produto = ttk.Combobox(
            self,
            width=47,
            values=self.lista_produtos)
        self.combobox_produto.insert(0, "Produto")
        self.combobox_produto.pack(pady=2)

        self.lista_fornecedores: list = self.data_manager.get_nome_fornecedores()
        self.lista_fornecedores = list(set(self.lista_fornecedores))

        self.combobox_fornecedor = ttk.Combobox(
            self,
            width=47,
            values=self.lista_fornecedores)
        self.combobox_fornecedor.insert(0, "Fornecedor")
        self.combobox_fornecedor.pack(pady=2)

        self.spinbox_quantidade = ttk.Spinbox(
            self,
            from_=1,
            to=99,
            width=45)
        self.spinbox_quantidade.insert(0, "Quantidade")
        self.spinbox_quantidade.pack(pady=2)

        self.entry_preco = ttk.Entry(
            self,
            width=49,
        )
        self.entry_preco.insert(0, f"Preço de Compra")
        self.entry_preco.pack(pady=2)

        self.today: date = date.today()
        self.current_date: str = str(self.today.strftime("%d/%m/%Y"))

        self.current_time: str = str(datetime.now().strftime("%H:%M:%S"))

        self.date_entry = ttk.DateEntry(
            master=self,
            startdate=self.today,
            dateformat=r"%d/%m/%Y",
            bootstyle=DEFAULT,
        )
        self.date_entry.pack(pady=2)

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Comprar!",
            width=47,
            command=self.popup_confirmacao
        )
        self.btn_action.pack(pady=2)

        self.btn_delete = ttk.Button(
            self,
            style="danger.TButton",
            text="Deletar registros selecionados",
            width=47,
            command=self._bind_delete
        )
        self.btn_delete.pack(pady=2)

    def update_tree(self):
        self.clean_tree()
        registros: list = self.data_manager.get_compras()
        for row in registros:
            self.tree.insert(
                parent='',
                index=END,
                iid=row[0],
                values=row
            )

    def clean_tree(self):
        self.tree.delete(*self.tree.get_children())

    def _bind_delete(self):
        to_delete: list = []
        for iid in self.tree.selection():
            row: str = self.tree.item(iid, 'values')
            to_delete.append(row[0])
        self.data_manager.delete_row(
            dataframe_name="compras",
            ids_to_delete=to_delete
        )
        self.update_tree()

    def popup_confirmacao(self):
        row_compra = ','.join([
            self.combobox_produto.get(),
            self.combobox_fornecedor.get(),
            self.entry_preco.get(),
            self.spinbox_quantidade.get(),
            self.date_entry.entry.get(),
            self.current_time
        ])

        confirmation: bool = tkinter.messagebox.askyesno(
            title="ATENÇÃO!",
            message=f"Confirma que os dados estão corretos?"
        )
        if confirmation:
            self.data_manager.insert_row(3, row_compra)
            self.update_tree()

            showinfo(
                title="SUCESSO!",
                message="Cadastro realizado com sucesso!"
            )
        else:
            print("Dados não confirmados.")


class CadastroVendas(ttk.Frame):
    def __init__(self, data_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.tree = ttk.Treeview(
            master=self,
            style=INFO
        )
        self.tree['columns'] = ("id", "produto", "fornecedor", "preco_venda", "qtd", "data", "tempo")
        self.tree.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree.column("id", anchor=CENTER, width=20, minwidth=0)
        self.tree.column("produto", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("fornecedor", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("preco_venda", anchor=CENTER, width=40, minwidth=0)
        self.tree.column("qtd", anchor=CENTER, width=40, minwidth=0)
        self.tree.column("data", anchor=CENTER, width=80, minwidth=0)
        self.tree.column("tempo", anchor=CENTER, width=80, minwidth=0)
        self.tree.heading("#0", text="Label")
        self.tree.heading("id", text="ID")
        self.tree.heading("produto", text="Produto")
        self.tree.heading("fornecedor", text="Fornecedor")
        self.tree.heading("preco_venda", text="Preço")
        self.tree.heading("qtd", text="Quant.")
        self.tree.heading("data", text="Data")
        self.tree.heading("tempo", text="Hora")
        self.tree.pack(padx=30, pady=5, fill=BOTH, expand=YES)
        self.update_tree()

        self.lbl_title = ttk.Label(
            self,
            text=f"REGISTRAR VENDAS",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack(pady=5)

        self.lista_produtos: list = self.data_manager.get_nome_produtos()
        self.lista_produtos = list(set(self.lista_produtos))

        self.combobox_produto = ttk.Combobox(
            self,
            width=47,
            values=self.lista_produtos)
        self.combobox_produto.insert(0, "Produto")
        self.combobox_produto.pack(pady=2)

        self.lista_fornecedores: list = self.data_manager.get_nome_fornecedores()
        self.lista_fornecedores = list(set(self.lista_fornecedores))

        self.combobox_fornecedor = ttk.Combobox(
            self,
            width=47,
            values=self.lista_fornecedores)
        self.combobox_fornecedor.insert(0, "Fornecedor")
        self.combobox_fornecedor.pack(pady=2)

        self.spinbox_quantidade = ttk.Spinbox(
            self,
            from_=1,
            to=99,
            width=45)
        self.spinbox_quantidade.insert(0, "Quantidade")
        self.spinbox_quantidade.pack(pady=2)

        self.entry_preco = ttk.Entry(
            self,
            width=49,
        )
        self.entry_preco.insert(0, f"Preço de Venda")
        self.entry_preco.pack(pady=2)

        self.today: date = date.today()
        self.current_date: str = str(self.today.strftime("%d/%m/%Y"))

        self.current_time: str = str(datetime.now().strftime("%H:%M:%S"))

        self.date_entry = ttk.DateEntry(
            master=self,
            startdate=self.today,
            dateformat=r"%d/%m/%Y",
            bootstyle=DEFAULT,
        )
        self.date_entry.pack(pady=2)

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Vendido!",
            width=47,
            command=self.popup_confirmacao
        )
        self.btn_action.pack(pady=2)

        self.btn_delete = ttk.Button(
            self,
            style="danger.TButton",
            text="Deletar registros selecionados",
            width=47,
            command=self._bind_delete
        )
        self.btn_delete.pack(pady=2)

    def update_tree(self):
        self.clean_tree()
        registros: list = self.data_manager.get_vendas()
        for row in registros:
            self.tree.insert(
                parent='',
                index=END,
                iid=row[0],
                values=row
            )

    def clean_tree(self):
        self.tree.delete(*self.tree.get_children())

    def _bind_delete(self):
        to_delete: list = []
        for iid in self.tree.selection():
            row: str = self.tree.item(iid, 'values')
            to_delete.append(row[0])
        self.data_manager.delete_row(
            dataframe_name="vendas",
            ids_to_delete=to_delete
        )
        self.update_tree()

    def popup_confirmacao(self):
        row_compra = ','.join([
            self.combobox_produto.get(),
            self.combobox_fornecedor.get(),
            self.entry_preco.get(),
            self.spinbox_quantidade.get(),
            self.date_entry.entry.get(),
            self.current_time
        ])

        confirmation: bool = tkinter.messagebox.askyesno(
            title="ATENÇÃO!",
            message=f"Confirma que os dados estão corretos?"
        )
        if confirmation:
            self.data_manager.insert_row(4, row_compra)
            self.update_tree()
        else:
            print("Dados não confirmados.")


class Cadastro(ttk.Frame):
    def __init__(self, data_manager=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.cadastro_produto = CadastroProduto(
            master=self,
            data_manager=self.data_manager
        )
        self.cadastro_produto.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        self.cadastro_fornecedores = CadastroFornecedor(
            master=self,
            data_manager=self.data_manager
        )
        self.cadastro_fornecedores.pack(
            side=RIGHT,
            fill=BOTH,
            expand=True
        )


class CadastroProduto(ttk.Frame):
    def __init__(self, data_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager: DataManager = data_manager

        self.tree_produtos = ttk.Treeview(
            master=self,
            style=INFO
        )
        self.tree_produtos['columns'] = ('ID', 'Nome', 'Fornecedor')
        self.tree_produtos.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree_produtos.column("ID", anchor=CENTER, width=40, minwidth=0)
        self.tree_produtos.column("Nome", anchor=CENTER, width=150, minwidth=0)
        self.tree_produtos.column("Fornecedor", anchor=CENTER, width=150, minwidth=0)
        self.tree_produtos.heading("#0", text="Label")
        self.tree_produtos.heading("ID", text="ID")
        self.tree_produtos.heading("Nome", text="Nome")
        self.tree_produtos.heading("Fornecedor", text="Fornecedor")
        self.tree_produtos.pack(padx=30, pady=10, fill=BOTH, expand=YES)
        self.update_tree()

        self.lbl_title = ttk.Label(
            self,
            text=f"CADASTRAR NOVO PRODUTO",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack(pady=(30, 20))

        self.novo_produto = ttk.Entry(
            master=self,
            width=49
        )
        self.novo_produto.insert(0, "Nome do Novo Produto")
        self.novo_produto.pack(pady=5)

        self.nome_fornecedores: list = self.data_manager.get_nome_fornecedores()
        self.nome_fornecedores = list(set(self.nome_fornecedores))

        self.combobox_fornecedor = ttk.Combobox(
            self,
            width=47,
            values=self.nome_fornecedores
        )
        self.combobox_fornecedor.insert(0, "Fornecedores")
        self.combobox_fornecedor.pack(pady=5)

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Cadastrar Produto!",
            width=47,
            command=self.popup_confirmacao
        )
        self.btn_action.pack(pady=5)

        self.btn_delete = ttk.Button(
            master=self,
            command=self._bind_delete,
            text="Deletar produtos selecionados!",
            width=47,
            style=DANGER
        )
        self.btn_delete.pack(pady=5)

    def update_tree(self):
        self.clean_tree()
        produtos: list = self.data_manager.get_produtos()
        for row in produtos:
            self.tree_produtos.insert(
                parent='',
                index=END,
                values=row
            )

    def clean_tree(self):
        self.tree_produtos.delete(*self.tree_produtos.get_children())

    def _bind_delete(self):
        to_delete: list = []
        for iid in self.tree_produtos.selection():
            row: str = self.tree_produtos.item(iid, 'values')
            to_delete.append(row[0])
        self.data_manager.delete_row(
            "produtos",
            ids_to_delete=to_delete
        )
        self.update_tree()

    def popup_confirmacao(self):
        self.row_produto = f"{self.novo_produto.get()},{self.combobox_fornecedor.get()}"

        confirmation: bool = tkinter.messagebox.askyesno(
            title="ATENÇÃO!",
            message=f"Confirma que os dados estão corretos?"
        )
        if confirmation:
            self.data_manager.insert_row(2, self.row_produto)
            self.update_tree()

            showinfo(
                title="SUCESSO!",
                message="Cadastro realizado com sucesso!"
            )
        else:
            print("Dados não confirmados.")

        '''BOTAR OS WIDGETS FINAIS AQUI'''


class CadastroFornecedor(ttk.Frame):
    def __init__(self, data_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager

        self.tree_fornecedores = ttk.Treeview(
            master=self,
            bootstyle=INFO
        )
        self.tree_fornecedores['columns'] = ('ID', 'Fornecedor')
        self.tree_fornecedores.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree_fornecedores.column("ID", anchor=CENTER, width=10, minwidth=0)
        self.tree_fornecedores.column("Fornecedor", anchor=CENTER, width=150, minwidth=0)
        self.tree_fornecedores.heading("#0", text="Label")
        self.tree_fornecedores.heading("ID", text="ID")
        self.tree_fornecedores.heading("Fornecedor", text="Fornecedor")
        self.tree_fornecedores.pack(padx=30, pady=10, fill=BOTH, expand=YES)
        self.update_tree()

        self.lbl_title = ttk.Label(
            self,
            text=f"CADASTRAR NOVO FORNECEDOR",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack(pady=(30, 20))

        self.novo_fornecedor = ttk.Entry(
            master=self,
            width=49
        )
        self.novo_fornecedor.insert(0, "Nome do Novo Fornecedor")
        self.novo_fornecedor.pack(pady=10)

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Cadastrar Fornecedor!",
            width=47,
            command=self.popup_confirmacao
        )
        self.btn_action.pack(pady=10)

        self.btn_delete = ttk.Button(
            master=self,
            command=self._bind_delete,
            text="Deletar fornecedores selecionados!",
            width=47,
            style=DANGER
        )
        self.btn_delete.pack(pady=(10, 20))

    def update_tree(self):
        self.clean_tree()
        fornecedores: list = self.data_manager.get_fornecedores()
        for row in fornecedores:
            self.tree_fornecedores.insert(
                parent='',
                index=END,
                iid=row[0],
                values=row
            )

    def clean_tree(self):
        self.tree_fornecedores.delete(*self.tree_fornecedores.get_children())

    def _bind_delete(self):
        to_delete: list = []
        for iid in self.tree_fornecedores.selection():
            row: str = self.tree_fornecedores.item(iid, 'values')
            to_delete.append(row[0])
        self.data_manager.delete_row(
            "fornecedores",
            ids_to_delete=to_delete
        )
        self.update_tree()

    def popup_confirmacao(self):

        self.row_fornecedor = f"{self.novo_fornecedor.get()}"

        confirmation: bool = tkinter.messagebox.askyesno(
            title="ATENÇÃO!",
            message=f"Confirma que os dados estão corretos?"
        )
        if confirmation:
            self.data_manager.insert_row(1, self.row_fornecedor)
            self.update_tree()

            showinfo(
                title="SUCESSO!",
                message="Cadastro realizado com sucesso!"
            )
        else:
            print("Dados não confirmados.")


class CadastroCompraVenda(ttk.Frame):
    def __init__(self, data_manager, compra_ou_venda: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_manager = data_manager
        self.compra_ou_venda = compra_ou_venda

        self.tree = ttk.Treeview(
            master=self,
            bootstyle=INFO
        )
        self.tree['columns'] = ("id", "produto", "fornecedor", "preco_compra", "qtd", "data", "tempo")
        self.tree.column("#0", anchor=CENTER, width=0, minwidth=0, stretch=NO)
        self.tree.column("id", anchor=CENTER, width=10, minwidth=0)
        self.tree.column("produto", anchor=CENTER, width=150, minwidth=0)
        self.tree.column("fornecedor", anchor=CENTER, width=150, minwidth=0)
        self.tree.column("preco_compra", anchor=CENTER, width=150, minwidth=0)
        self.tree.column("qtd", anchor=CENTER, width=150, minwidth=0)
        self.tree.column("data", anchor=CENTER, width=150, minwidth=0)
        self.tree.column("tempo", anchor=CENTER, width=150, minwidth=0)
        self.tree.heading("#0", text="Label")
        self.tree.heading("id", text="ID")
        self.tree.heading("produto", text="")
        self.tree.heading("fornecedor", text="")
        self.tree.heading("preco_compra", text="")
        self.tree.heading("qtd", text="")
        self.tree.heading("data", text="")
        self.tree.heading("tempo", text="")
        self.tree.pack(padx=30, pady=10, fill=BOTH, expand=YES)
        self.update_tree()

        self.lbl_title = ttk.Label(
            self,
            text=f"REGISTRAR {self.compra_ou_venda.upper()}",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack()

        self.lista_produtos: list = self.data_manager.getpr()[
            0]
        self.lista_produtos = list(set(self.lista_produtos))

        self.combobox_produto = ttk.Combobox(
            self,
            width=47,
            values=self.lista_produtos
        )
        self.combobox_produto.insert(0, "Produto")
        self.combobox_produto.pack()

        self.lista_fornecedores: list = self.data_manager.get_nome_fornecedores()
        self.lista_fornecedores = list(set(self.lista_fornecedores))

        self.combobox_fornecedor = ttk.Combobox(
            self,
            width=47,
            values=self.lista_fornecedores
        )
        self.combobox_fornecedor.insert(0, "Fornecedor")
        self.combobox_fornecedor.pack()

        self.spinbox_quantidade = ttk.Spinbox(
            self,
            from_=1,
            to=99,
            width=45
        )
        self.spinbox_quantidade.insert(0, "Quantidade")
        self.spinbox_quantidade.pack()

        self.msg_preco: str = f"Preço de {self.compra_ou_venda.capitalize()}"
        self.venda: bool = self.compra_ou_venda.strip()[0] in "vV"
        self.msg_pers: str = "vendido" if self.venda else "comprado"

        self.entry_preco = ttk.Entry(
            self,
            width=49,
        )
        self.entry_preco.insert(0, self.msg_preco)
        self.entry_preco.pack()

        self.today: date = date.today()
        self.current_date: str = str(self.today.strftime("%d/%m/%Y"))

        self.current_time: str = str(datetime.now().strftime("%H:%M:%S"))

        self.date_entry = ttk.DateEntry(
            master=self,
            startdate=self.today,
            dateformat=r"%d/%m/%Y",
            bootstyle=DEFAULT,
        )
        self.date_entry.pack()

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Vendido!" if self.venda else "Comprado!",
            width=47,
            command=self.popup_confirmacao
        )
        self.btn_action.pack()

    def popup_confirmacao(self):

        row1 = f"{self.combobox_produto.get()},{self.combobox_fornecedor.get()},"
        row2 = f"{self.entry_preco.get()},{self.spinbox_quantidade.get()},"
        row3 = f"{self.date_entry.entry.get()},{self.current_time}"
        row_compra_venda: str = row1 + row2 + row3

        confirmation: bool = tkinter.messagebox.askyesno(
            title="ATENÇÃO!",
            message=f"Confirma que os dados estão corretos?"
        )
        if confirmation:
            print(self.venda)
            print(row_compra_venda)

            if self.venda:
                self.data_manager.insert_row(4, row_compra_venda)
            else:
                self.data_manager.insert_row(3, row_compra_venda)

            showinfo(
                title="SUCESSO!",
                message="Cadastro realizado com sucesso!"
            )
        else:
            print("Dados não confirmados.")
