import uuid
from csv import writer, reader
from tkinter import messagebox

import pandas as pd


class DataManager:
    def __init__(self):

        self.estoque_directory = "dados/estoque.csv"
        self.estoque_data: pd.DataFrame = pd.read_csv(self.estoque_directory)

        self.compras_directory = "dados/registro_compras.csv"
        self.compras_data: pd.DataFrame = pd.read_csv(self.compras_directory)

        self.vendas_directory = "dados/registro_vendas.csv"
        self.vendas_data: pd.DataFrame = pd.read_csv(self.vendas_directory)

        self.produtos_directory = "dados/produtos.csv"
        self.produtos_data: pd.DataFrame = pd.read_csv(self.produtos_directory)

        self.fornecedores_directory = "dados/fornecedores.csv"
        self.fornecedores_data: pd.DataFrame = pd.read_csv(self.fornecedores_directory)

        self.directory_dict: dict = {
            "estoque": self.estoque_directory,
            "fornecedores": self.fornecedores_directory,
            "produtos": self.produtos_directory,
            "compras": self.compras_directory,
            "vendas": self.vendas_directory
        }
        self.dataframe_dict: dict = {
            "estoque": self.estoque_data,
            "fornecedores": self.fornecedores_data,
            "produtos": self.produtos_data,
            "compras": self.compras_data,
            "vendas": self.vendas_data,
        }

    def update_estoque(self) -> None:
        self.estoque_data: pd.DataFrame = pd.read_csv(self.estoque_directory)

    def update_compras(self) -> None:
        self.compras_data: pd.DataFrame = pd.read_csv(self.compras_directory)

    def update_vendas(self) -> None:
        self.vendas_data: pd.DataFrame = pd.read_csv(self.vendas_directory)

    def update_produtos(self) -> None:
        self.produtos_data: pd.DataFrame = pd.read_csv(self.produtos_directory)

    def update_fornecedores(self) -> None:
        self.fornecedores_data: pd.DataFrame = pd.read_csv(
            self.fornecedores_directory)

    def update_data(self) -> None:
        self.update_estoque()
        self.update_produtos()
        self.update_vendas()
        self.update_compras()
        self.update_fornecedores()

    def insert_row(self, dir_index: int, row: str) -> None:
        """
        dir_index
        0: Estoque
        1: Fornecedores
        2: Produtos
        3: Registro Compras
        4: Registro Vendas
        """

        directories: list = [
            self.estoque_directory,
            self.fornecedores_directory,
            self.produtos_directory,
            self.compras_directory,
            self.vendas_directory
        ]

        id_generated = str(self.generate_id())
        row: list = row.split(",")
        row.insert(0, id_generated)

        all_right = True
        if dir_index == 3:
            self._add_on_estoque(row)
        elif dir_index == 4:
            try:
                self._remove_from_estoque(row)
            except ValueError:
                all_right = False

        if all_right:
            with open(file=directories[dir_index], mode="a", newline="\n") as file_object:
                writer_object = writer(file_object)
                writer_object.writerow(row)
                self.update_data()

    def delete_row(self, dataframe_name: str, ids_to_delete: list):
        """Deleta qualquer linha do dataframe que contenha o termo."""
        lines: list = []
        dir_data: str = self.directory_dict[dataframe_name]
        with open(file=dir_data, mode='r') as read_file:
            reader_object = reader(read_file)
            for row in reader_object:
                id_row = row[0]
                if not (id_row in ids_to_delete):
                    lines.append(row)
        with open(file=dir_data, mode='w', newline="") as write_file:
            writer_object = writer(write_file)
            writer_object.writerows(lines)
        self.update_data()

    def save_estoque_data(self) -> None:
        self.estoque_data.to_csv(self.estoque_directory, index=False)

    def get_fornecedores_name(self):
        """Pode haver o caso de haver fornecedores, mas estes não estiverem com produtos cadastrados."""
        return self.fornecedores_data["fornecedor"].tolist()

    def get_column_data_estoque(self, column_name: str) -> list:
        """colunas do estoque: id,produto,fornecedor,preco_compra,preco_venda,qtd,data,tempo"""
        return self.estoque_data[column_name].tolist()

    def get_produtos(self):
        """Retorna toda a planinha de produtos no formato list[list[str]]"""
        return self.produtos_data.to_numpy().tolist()

    def get_fornecedores(self):
        """Retorna toda a planinha de fornecedores no formato list[list[str]]"""
        return self.fornecedores_data.to_numpy().tolist()

    def get_compras(self):
        """Retorna toda a planinha de compras no formato list[list[str]]"""
        return self.compras_data.to_numpy().tolist()

    def get_vendas(self):
        """Retorna toda a planinha de vendas no formato list[list[str]]"""
        return self.vendas_data.to_numpy().tolist()

    def get_estoque(self):
        """Retorna toda a planinha de estoque no formato list[list[str]]"""
        return self.estoque_data.to_numpy().tolist()

    def get_nome_fornecedores(self):
        return self.fornecedores_data['fornecedor']

    def get_nome_produtos(self):
        return set(self.produtos_data['produto'])

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())[:5]

    def _add_on_estoque(self, row_compra: list):
        produto: str = row_compra[1]
        fornecedor: str = row_compra[2]
        filtro_produto = self.estoque_data['produto'] == produto
        filtro_fornecedor = self.estoque_data['fornecedor'] == fornecedor
        estoque = self.estoque_data[filtro_produto & filtro_fornecedor].to_numpy().tolist()
        if not estoque:
            row_compra.pop(0)
            row_compra.insert(3, '')
            self.insert_row(
                dir_index=0,
                row=','.join(row_compra)
            )
        else:
            estoque = estoque[0]
            iid = estoque[0]
            quantidade = int(estoque[5]) + int(row_compra[4])
            self.estoque_data.loc[self.estoque_data['id'] == iid, 'qtd'] = quantidade
        self.save_estoque_data()

    def _remove_from_estoque(self, row_venda: list):
        produto: str = row_venda[1]
        fornecedor: str = row_venda[2]
        filtro_produto = self.estoque_data['produto'] == produto
        filtro_fornecedor = self.estoque_data['fornecedor'] == fornecedor
        estoque = self.estoque_data[filtro_produto & filtro_fornecedor].to_numpy().tolist()
        if not estoque:
            messagebox.showerror(
                title="Erro!",
                message="Você não tem esse produto no estoque!"
            )
            raise ValueError
        else:
            estoque = estoque[0]
            iid = estoque[0]
            quantidade = int(estoque[5]) - int(row_venda[4])
            if quantidade < 0:
                messagebox.showerror(
                    title="Erro!",
                    message="Você não tem esse montante no estoque!"
                )
                raise ValueError
            else:
                self.estoque_data.loc[self.estoque_data['id'] == iid, 'qtd'] = quantidade
                self.save_estoque_data()
                messagebox.showinfo(
                    title="SUCESSO!",
                    message="Cadastro realizado com sucesso!"
                )


if __name__ == "__main__":
    data_manager = DataManager()
