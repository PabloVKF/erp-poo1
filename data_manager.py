import pandas as pd


class DataManager:
    def __init__(self):
        self.file_directory = "dados/registros.csv"
        self.data: pd.DataFrame = pd.read_csv(self.file_directory)
        # print(self.data.axes)

    def update_data(self) -> None:
        self.data: pd.DataFrame = pd.read_csv(self.file_directory)

    def insert_row(self, row: list[any]) -> None:
        pass

    def delete_row(self, column_name: str, item_name: str) -> None:
        self.data = self.data.set_index(column_name)
        self.data = self.data.drop(item_name, axis=0)

    def save_data(self) -> None:
        self.data.to_csv(self.file_directory)

    def get_column_data(self, column_name: str):
        """column_name: id, produto, fornecedor, preco_compra, preco_venda"""
        return self.data[column_name].tolist()


# print(DataManager().get_column_data("produto"))
# DataManager().delete_row("produto", "produto14")