from tkinter.messagebox import showwarning, askyesno, showinfo, showerror
from tkinter.font import BOLD
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from data_manager import DataManager


# Conforme solicitado pela fonte das imagens, links de referencia:
#   - Logo: "https://www.flaticon.com/br/autores/freepik"
#   - Vendas: "https://www.flaticon.com/br/autores/tomas-knop"
#   - Estoque: "https://www.flaticon.com/authors/icongeek26"
#   - Compras: "https://www.freepik.com"
#   - Configurações: "https://www.flaticon.com/authors/gregor-cresnar-premium"


class Appplication(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        # self.height_window = 720
        # self.width_window = 1280
        # self.position_right = int(self.winfo_screenwidth() / 2 - self.width_window / 2)
        # self.position_down = int(self.winfo_screenheight() / 2 - self.height_window / 2)
        # self.geometry(f"{self.width_window}x{self.height_window}+{self.position_right}+{self.position_down}")

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

        """HEADER"""
        self.header_frame = ttk.Frame(
            master=self,
            padding=20,
            bootstyle=SECONDARY
        )
        self.header_frame.grid(row=0, column=0, columnspan=4, sticky=EW)
        # self.header_frame.pack(side=LEFT)

        self.header_label = ttk.Label(
            master=self.header_frame,
            image="logo",
            bootstyle=(INVERSE, SECONDARY)
        )
        self.header_label.pack(side=LEFT)

        self.header_label_2 = ttk.Label(
            master=self.header_frame,
            text="Gerenciador de Estoque - Alunos: Marcos e Pablo",
            font=('TkDefaultFixed', 26),
            bootstyle=(INVERSE, SECONDARY)
        )
        self.header_label_2.pack(side=LEFT, padx=10)

        """MENU BAR"""

        self.menu_bar_frame = ttk.Frame(master=self)
        self.menu_bar_frame.grid(row=1, column=0, columnspan=4, sticky=EW)
        # self.menu_bar_frame.pack(side=BOTTOM)

        self.estoque_menu_button = ttk.Button(
            master=self.menu_bar_frame,
            image="estoque",
            text="Estoque",
            compound=LEFT,
            bootstyle=INFO,
            command=self.estoque_btn
        )
        self.estoque_menu_button.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        self.estoque_menu_button = ttk.Button(
            master=self.menu_bar_frame,
            image="compras",
            text="Compras & Vendas",
            compound=LEFT,
            bootstyle=INFO,
            command=self.compras_btn
        )
        self.estoque_menu_button.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        self.estoque_menu_button = ttk.Button(
            master=self.menu_bar_frame,
            image="configurações",
            text="Cadastro",
            compound=LEFT,
            bootstyle=INFO,
            command=self.vendas_btn
        )
        self.estoque_menu_button.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        # self.estoque_menu_button = ttk.Button(
        #     master=self.menu_bar_frame,
        #     image="configurações",
        #     text="Configurações",
        #     compound=LEFT,
        #     bootstyle=INFO,
        #     command=self.config_btn
        # )
        # self.estoque_menu_button.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        """BODY"""
        # CADASTRO DE VENDAS --------------------------------------------------
        self.body_frame = ttk.Frame(self)
        self.body_frame.grid(row=2, column=0, columnspan=4,
                             ipadx=100, ipady=300)

        lbl_fornecedor = ttk.Label(
            self.body_frame,
            text="CADASTRAR VENDA",
            font=("Arial", 24, BOLD)
        )
        lbl_fornecedor.pack()

        lista_produtos: list = DataManager().get_column_data("produto")
        combobox_produto = ttk.Combobox(
            self.body_frame,
            width=48,
            values=lista_produtos)
        combobox_produto.insert(0, "Produto")
        combobox_produto.pack()

        lista_fornecedores: list = DataManager().get_column_data("fornecedor")
        combobox_fornecedor = ttk.Combobox(
            self.body_frame,
            width=48,
            values=lista_fornecedores)
        combobox_fornecedor.insert(0, "Fornecedor")
        combobox_fornecedor.pack()

        spinbox_quantidade = ttk.Spinbox(
            self.body_frame,
            from_=1,
            to=100,
            width=46)
        spinbox_quantidade.insert(0, "Quantidade")
        spinbox_quantidade.pack()

        meter_preco_venda = ttk.Meter(
            self.body_frame,
            bootstyle=INFO,
            interactive=True,
            subtext="Preço de Venda",
            textleft="R$",
            stepsize=0.01
        ).pack()

        entry_preco_venda = ttk.Entry(
            self.body_frame,
            width=50
        )
        entry_preco_venda.insert(0, "Preço de Venda")
        entry_preco_venda.pack()

        btn_vendido = ttk.Button(
            self.body_frame,
            style="success.TButton",
            # bootsyle="success",
            text="Vendido!",
            width=48,
            command=self.vendido
        )
        btn_vendido.pack()

        # self.body_frame.pack(side=BOTTOM)

    def compras_btn(self):
        print("Clicou nas Compras.")

    def estoque_btn(self):
        print("Clicou no Estoque.")

    def vendas_btn(self):
        print("Clicou nas Vendas.")

    def config_btn(self):
        print("Clicou nas Configurações.")
    
    def vendido(self):
        askyesno(message="Confirma que os dados estão corretos?")
        # print(f"O produto {} do fornecedor {} foi vendido em {} unidade(s) a um preço de R${}.")
