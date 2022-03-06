from csv import writer

import pandas as pd
import uuid


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
        self.fornecedores_data: pd.DataFrame = pd.read_csv(
            self.fornecedores_directory
        )

    def update_data(self) -> None:
        self.estoque_data: pd.DataFrame = pd.read_csv(self.estoque_directory)

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

        id = str(self.generate_id())[:5]
        row: list = row.split(",")
        row.insert(0, id)

        with open(directories[dir_index], "a", newline="\n") as file_object:
            writer_object = writer(file_object)
            writer_object.writerow(row)

    def delete_row(self, index_data: int):
        with open(self.estoque_directory, "r") as file:
            r: list = file.read().split()
            for line in r:
                print(line)
            file = r.pop(index_data)

    def delete_item_everywhere(self, column_name: str, item_name: str) -> None:
        """
        Apaga todas as linhas que possuem item_name.
        O correto seria passar apenas o index ou id da linha a ser deletada.
        column_name: "produto"
        item_name:   "Camiseta"
        """
        self.estoque_data = self.estoque_data.set_index(column_name)
        self.estoque_data = self.estoque_data.drop(item_name, axis=0)

    def save_data(self) -> None:
        self.estoque_data.to_csv(self.estoque_directory)

    def get_produtos_and_fornecedor(self):
        """Retorna duas listas. A primeira, produtos já cadastrados sem repetição,
        enquanto a segunda, seus respectivos fornecedores, mas sem repetição."""
        return self.produtos_data["produto"].tolist(), self.produtos_data["fornecedor"].tolist()

    def get_fornecedores(self):
        """Pode haver o caso de haver fornecedores, mas estes não estiverem com produtos cadastrados."""
        return self.fornecedores_data["fornecedor"].tolist()

    def get_column_data_estoque(self, column_name: str) -> list:
        """colunas do estoque: id,produto,fornecedor,preco_compra,preco_venda,qtd,data,tempo"""
        return self.estoque_data[column_name].tolist()

    @staticmethod
    def generate_id():
        return uuid.uuid4()


if __name__ == "__main__":
    data_manager = DataManager()
    t = data_manager.get_produtos_and_fornecedor()[0]
    print(t)
