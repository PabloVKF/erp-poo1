import pandas as pd
from typing import List


class DataManeger:
    def __init__(self):
        self.registros: pd.DataFrame = pd.read_csv("dados/registros.csv",
                                                   sep=",",
                                                   index_col='id', )
        print(self.registros.head())

    def update_data(self) -> None:
        self.registros: pd.DataFrame = pd.read_csv("dados/registros.csv",
                                                   sep=",",
                                                   index_col='id')

    def insert_row(self, row: List[any]) -> None:
        pass

    def delte_row(self) -> None:
        pass

    def save_data(self) -> None:
        self.registros.to_csv("dados/registros.csv")
