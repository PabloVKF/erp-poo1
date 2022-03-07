from csv import writer, reader
import pandas as pd
import uuid


class DataManager:
    def __init__(self):

        self.estoque_directory = "dados/estoque.csv"
        self.estoque_data: pd.DataFrame = pd.read_csv(
            self.estoque_directory, index_col="id")

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

        id = str(self.generate_id())[:5]
        row: list = row.split(",")
        row.insert(0, id)

        with open(file=directories[dir_index], mode="a", newline="\n") as file_object:
            writer_object = writer(file_object)
            writer_object.writerow(row)

        self.update_data()

    def delete_row(self, dataframe_name: str, term_to_delete: str):
        """Deleta qualquer linha do dataframe que contenha o termo."""
        lines: list = []
        dir: pd.DataFrame = self.directory_dict[dataframe_name]
        with open(file=dir, mode='r') as readFile:
            reader_object = reader(readFile)
            for row in reader_object:
                lines.append(row)
                for field in row:
                    if field == term_to_delete:
                        lines.remove(row)
        with open(file=dir, mode='w', newline="") as writeFile:
            writer_object = writer(writeFile)
            writer_object.writerows(lines)

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

    @staticmethod
    def generate_id():
        return uuid.uuid4()


if __name__ == "__main__":
    data_manager = DataManager()
