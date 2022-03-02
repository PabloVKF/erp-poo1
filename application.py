import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from data_maneger import DataManeger


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

        self.datamaneger = DataManeger()

        self.images = [
            ttk.PhotoImage(
                name="logo",
                file="imagens/erp_64px.png"),
            ttk.PhotoImage(
                name="estoque",
                file="imagens/boxes_24px.png"),
            ttk.PhotoImage(
                name="vendas",
                file="imagens/cofrinho_24px.png"),
            ttk.PhotoImage(
                name="configurações",
                file="imagens/settings_24px.png"),
            ttk.PhotoImage(
                name="compras",
                file="imagens/shopping-cart_24px.png")
        ]

        """HEADER"""
        self.header_frame = ttk.Frame(
            master=self,
            padding=20,
            bootstyle=SECONDARY
        )
        self.header_frame.grid(row=0, column=0, columnspan=4, sticky=EW)

        self.hdr_label = ttk.Label(
            master=self.header_frame,
            image="logo",
            bootstyle=(INVERSE, SECONDARY)
        )
        self.hdr_label.pack(side=LEFT)

        self.hdr_label_2 = ttk.Label(
            master=self.header_frame,
            text="Bem vindo!",
            font=('TkDefaultFixed', 30),
            bootstyle=(INVERSE, SECONDARY)
        )
        self.hdr_label_2.pack(side=LEFT, padx=10)

        """MENU BAR"""
        self.menu_bar_frame = ttk.Frame(master=self)
        self.menu_bar_frame.grid(row=1, column=0, columnspan=4, sticky=EW)

        self.estoque_menu_buttom = ttk.Button(
            master=self.menu_bar_frame,
            image="estoque",
            text="Estoque",
            compound=LEFT,
            bootstyle=INFO,
            command=self.test
        )
        self.estoque_menu_buttom.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        self.estoque_menu_buttom = ttk.Button(
            master=self.menu_bar_frame,
            image="compras",
            text="Compras",
            compound=LEFT,
            bootstyle=INFO,
            command=self.test
        )
        self.estoque_menu_buttom.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        self.estoque_menu_buttom = ttk.Button(
            master=self.menu_bar_frame,
            image="vendas",
            text="Vendas",
            compound=LEFT,
            bootstyle=INFO,
            command=self.test
        )
        self.estoque_menu_buttom.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        self.estoque_menu_buttom = ttk.Button(
            master=self.menu_bar_frame,
            image="configurações",
            text="Configurações",
            compound=LEFT,
            bootstyle=INFO,
            command=self.test
        )
        self.estoque_menu_buttom.pack(side=LEFT, fill=BOTH, ipadx=100, ipady=5)

        """BODY"""
        self.body_frame = ttk.Frame(self)
        self.body_frame.grid(row=2, column=0, columnspan=4, ipadx=100, ipady=300)

    def test(self):
        print("Hello there!")
