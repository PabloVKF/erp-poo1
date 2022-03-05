import tkinter.messagebox
from tkinter.messagebox import *
from tkinter.font import BOLD
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from data_manager import DataManager
from constantes.directory_paths import *


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

        self.body = Body(self)
        self.body.pack(
            side=BOTTOM,
            fill=BOTH,
            expand=True
        )


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
            bootstyle=(INVERSE, SECONDARY)
        )
        self.header_label.pack(side=LEFT)

        self.header_label_2 = ttk.Label(
            master=self,
            text="Gerenciador de Estoque - Alunos: Marcos e Pablo",
            font=('TkDefaultFixed', 26),
            bootstyle=(INVERSE, SECONDARY)
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def destroy_widget_children(self):
        for children in self.winfo_children():
            children.destroy()

    def init_estoque(self):
        self.destroy_widget_children()

    def init_compras_vendas(self):
        self.destroy_widget_children()

    def init_cadastro(self):
        self.destroy_widget_children()
        self.cadastro = Cadastro(self)
        self.cadastro.pack()


class Cadastro(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vendas = CadastroCompraVenda(
            master=self,
            venda_ou_compra="venda"
        )
        self.vendas.pack(ipadx=99, ipady=50, pady=50)

        self.compras = CadastroCompraVenda(
            master=self,
            venda_ou_compra="compra"
        )
        self.compras.pack(ipadx=99, ipady=100)



class CadastroCompraVenda(ttk.Frame):
    def __init__(self, venda_ou_compra: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.venda_ou_compra = venda_ou_compra

        self.lbl_title = ttk.Label(
            self,
            text=f"CADASTRAR {self.venda_ou_compra.upper()}",
            font=("Arial", 23, BOLD)
        )
        self.lbl_title.pack()

        self.lista_produtos: list = DataManager().get_column_data("produto")
        self.lista_produtos = list(set(self.lista_produtos))

        self.combobox_produto = ttk.Combobox(
            self,
            width=47,
            values=self.lista_produtos)
        self.combobox_produto.insert(-1, "Produto")
        self.combobox_produto.pack()

        self.lista_fornecedores: list = DataManager().get_column_data("fornecedor")
        self.lista_fornecedores = list(set(self.lista_fornecedores))

        self.combobox_fornecedor = ttk.Combobox(
            self,
            width=47,
            values=self.lista_fornecedores)
        self.combobox_fornecedor.insert(-1, "Fornecedor")
        self.combobox_fornecedor.pack()

        self.spinbox_quantidade = ttk.Spinbox(
            self,
            from_=0,
            to=99,
            width=45)
        self.spinbox_quantidade.insert(-1, "Quantidade")
        self.spinbox_quantidade.pack()

        self.msg_preco = f"Preço de {self.venda_ou_compra.capitalize()}"
        self.venda = self.venda_ou_compra.strip()[-1]
        self.msg_pers = "vendido" if self.venda else "comprado"

        self.entry_preco = ttk.Entry(
            self,
            width=49,
        )
        self.entry_preco.insert(0, self.msg_preco)
        self.entry_preco.pack()

        self.btn_action = ttk.Button(
            self,
            style="success.TButton",
            text="Vendido!" if self.venda in "vV" else "Comprado!",
            width=47,
            command=self.popup_confirmacao_venda
        )
        self.btn_action.pack()

    def popup_confirmacao_venda(self):
        confirmation = tkinter.messagebox.askyesno(
            title="Confirma que os dados estão corretos?",
            message=f"Produto: {self.combobox_produto.get()}\n"
                    f"Fornecedor: {self.combobox_fornecedor.get()}\n"
                    f"Quantidade: {self.spinbox_quantidade.get()}\n"
                    f"Preço de {self.venda_ou_compra.capitalize()}: {self.entry_preco_venda.get()}"
        )
        if confirmation:
            tkinter.messagebox.showinfo(
                title="Dados confirmados.",
                message=f"O produto {self.combobox_produto.get()} do fornecedor {self.combobox_fornecedor.get()} foi "
                        f"vendido em {self.spinbox_quantidade.get()} unidade(s) a um preço "
                        f"de R${self.entry_preco_venda.get()}. "
            )
        else:
            print("Dados não confirmados.")
