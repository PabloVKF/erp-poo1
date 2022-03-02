from tkinter.messagebox import showwarning, askyesno, showinfo, showerror
from tkinter.font import BOLD
from ttkbootstrap.constants import *

from data_manager import DataManager

import ttkbootstrap as ttk


class Appplication(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack(fill=BOTH, expand=YES)

        Header(self)

        MenuBar(self)

        """BODY"""

        CadastroVendas(self)


class Header:

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)

        images_directory = "imagens/"
        master.images = [
            ttk.PhotoImage(
                name="logo",
                file=images_directory + "erp_64px.png"),
            ttk.PhotoImage(
                name="estoque",
                file=images_directory + "boxes_24px.png"),
            ttk.PhotoImage(
                name="vendas",
                file=images_directory + "cofrinho_24px.png"),
            ttk.PhotoImage(
                name="configurações",
                file=images_directory + "settings_24px.png"),
            ttk.PhotoImage(
                name="compras",
                file=images_directory + "shopping-cart_24px.png")
        ]

        self = ttk.Frame(
            master=master,
            padding=20,
            bootstyle=SECONDARY
        )
        # self.configure(padding=20)
        self.grid(row=0, column=0, columnspan=4, sticky=EW)
        # self.pack(side=LEFT)

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


class MenuBar:

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # LARGURA DO APP = 3*100px (3 botões HEADER) = 300px
        largura_botao = 150  # px
        altura_botao = 7  # px
        # ALTURA (ABAIXO) DEFINIDA PELO FRAME BODY (ipady)

        def compras_btn():
            print("Clicou nas Compras & Vendas.")

        def estoque_btn():
            print("Clicou no Estoque.")

        def cadastro_btn():
            print("Clicou no Cadastro.")

        self = ttk.Frame(master)
        self.grid(row=1, column=0, columnspan=4, sticky=EW)
        # self.pack(side=BOTTOM)

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="estoque",
            text="Estoque",
            compound=LEFT,
            bootstyle=INFO,
            command=estoque_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT, fill=BOTH, ipadx=largura_botao, ipady=altura_botao)

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="compras",
            text="Compras & Vendas",
            compound=LEFT,
            bootstyle=INFO,
            command=compras_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT, fill=BOTH, ipadx=largura_botao, ipady=altura_botao)

        self.estoque_menu_button = ttk.Button(
            master=self,
            image="configurações",
            text="Cadastro",
            compound=LEFT,
            bootstyle=INFO,
            command=cadastro_btn
        )
        self.estoque_menu_button.pack(
            side=LEFT, fill=BOTH, ipadx=largura_botao, ipady=altura_botao)


# QUERIA COLOCAR A CLASSE CadastroVendas DENTRO DA CLASSE Body, MAS N SEI COMO FAZ
# class Body:

#     def __init__(self, master, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     CadastroVendas()


def popup_yes_no(message: str):
    askyesno(message=message)
    # print(f"O produto {} do fornecedor {} foi vendido em {} unidade(s) a um preço de R${}.")


class CadastroVendas:

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self = ttk.Frame(master)
        self.grid(row=2, column=0, columnspan=4, ipadx=100, ipady=300)

        lbl_fornecedor = ttk.Label(
            self,
            text="CADASTRAR VENDA",
            font=("Arial", 24, BOLD)
        )
        lbl_fornecedor.pack()

        lista_produtos: list = DataManager().get_column_data("produto")
        combobox_produto = ttk.Combobox(
            self,
            width=48,
            values=lista_produtos)
        combobox_produto.insert(0, "Produto")
        combobox_produto.pack()

        lista_fornecedores: list = DataManager().get_column_data("fornecedor")
        combobox_fornecedor = ttk.Combobox(
            self,
            width=48,
            values=lista_fornecedores)
        combobox_fornecedor.insert(0, "Fornecedor")
        combobox_fornecedor.pack()

        spinbox_quantidade = ttk.Spinbox(
            self,
            from_=1,
            to=100,
            width=46)
        spinbox_quantidade.insert(0, "Quantidade")
        spinbox_quantidade.pack()

        entry_preco_venda = ttk.Entry(
            self,
            width=50,
        )
        entry_preco_venda.insert(0, "Preço de Venda")
        entry_preco_venda.pack()

        btn_vendido = ttk.Button(
            self,
            style="success.TButton",
            # bootsyle=SUCCESS,
            text="Vendido!",
            width=48,
            command=lambda: popup_yes_no(
                "Confirma que os dados estão corretos?")
        )
        btn_vendido.pack()
