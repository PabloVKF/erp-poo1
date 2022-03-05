from csv import writer

import pandas as pd
import uuid


class DataManager:
    def __init__(self):
        self.file_directory = "dados/estoque.csv"
        self.data: pd.DataFrame = pd.read_csv(self.file_directory)

    def update_data(self) -> None:
        self.data: pd.DataFrame = pd.read_csv(self.file_directory)

    def insert_row(self, row: str) -> None:
        """
        Exemplo de row:\n
        row = "Camiseta,Havan,7.00,8.18,16,26/02/2022,01:24:00"\n
        (sem o id)
        """
        row: list = row.split(",")
        id = str(self.generate_id())[:5]
        row.insert(0, id)
        with open(self.file_directory, "a", newline="\n") as file_object:
            writer_object = writer(file_object)
            writer_object.writerow(row)

    def delete_row(self, index_data: int):
        with open(self.file_directory, "r") as file:
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
        self.data = self.data.set_index(column_name)
        self.data = self.data.drop(item_name, axis=0)

    def save_data(self) -> None:
        self.data.to_csv(self.file_directory)

    def get_column_data(self, column_name: str) -> list:
        """column_name: id,produto,fornecedor,preco_compra,preco_venda,qtd,data,tempo"""
        return self.data[column_name].tolist()

    @staticmethod
    def generate_id():
        return uuid.uuid4()


if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.delete_row(10)
