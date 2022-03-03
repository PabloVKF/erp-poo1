from tkinter.messagebox import showwarning, askyesno, showinfo, showerror
from tkinter.font import BOLD
from ttkbootstrap.constants import *

from data_manager import DataManager

import ttkbootstrap as ttk


class Appplication(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data_manager = DataManager()

        self.pack(fill=BOTH, expand=YES)

        self.images_directory = "imagens/"
        self.images = [
            ttk.PhotoImage(
                name="logo",
                file=self.images_directory + "erp_64px.png"),
            ttk.PhotoImage(
                name="estoque",
                file=self.images_directory + "boxes_24px.png"),
            ttk.PhotoImage(
                name="vendas",
                file=self.images_directory + "cofrinho_24px.png"),
            ttk.PhotoImage(
                name="configurações",
                file=self.images_directory + "settings_24px.png"),
            ttk.PhotoImage(
                name="compras",
                file=self.images_directory + "shopping-cart_24px.png")
        ]

        header = Header(
            master=self,
            padding=20,
            bootstyle=SECONDARY
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            sticky=EW
        )

        # menu_bar = MenuBar(
        #     master=header
        # ).grid(
        #     row=1,
        #     column=0,
        #     columnspan=4,
        #     sticky=EW
        # )

        cadastro_vendas = CadastroVendas(
            master=self
        ).grid(
            row=2,
            column=0,
            columnspan=4,
            ipadx=100,
            ipady=200
        )


class Header(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

        largura_botao = 150  # px
        altura_botao = 7  # px

        def compras_btn():
            print("Clicou nas Compras & Vendas.")

        def estoque_btn():
            print("Clicou no Estoque.")

        def cadastro_btn():
            print("Clicou no Cadastro.")

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


class Body(ttk.Frame):
    pass


def popup_yes_no(msg_question: str, msg_conclusion: str):
    confirma_dados: bool = askyesno(message=msg_question)
    print("Dados confirmados.") if confirma_dados else print(
        "Dados não confirmados.")
    msg_conclusao = showinfo(message=msg_conclusion)


class CadastroVendas(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            text="Vendido!",
            width=48,
            command=lambda: popup_yes_no(
                msg_question=f"""Confirma que os dados estão corretos?\n
            Produto: {combobox_produto.get()}
            Fornecedor: {combobox_fornecedor.get()}
            Quantidade: {spinbox_quantidade.get()}
            Preço de Venda: {entry_preco_venda.get()}""",
                msg_conclusion=f"O produto {combobox_produto.get()} do fornecedor {combobox_fornecedor.get()} foi vendido em {spinbox_quantidade.get()} unidade(s) a um preço de R${entry_preco_venda.get()}."
            )
        )
        btn_vendido.pack()
