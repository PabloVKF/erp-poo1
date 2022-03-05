from datetime import datetime, timedelta
from random import randrange, randint, random, choice


def random_date(start, end):
    "referencia: https://www.codegrepper.com/code-examples/python/random+date+python"
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def datetime_generator(date_start: datetime, date_end: datetime):
    """Formato da data: dia/mês/ano\n
    referencia: https://www.codegrepper.com/code-examples/python/random+date+python"""
    d1 = datetime.strptime(f'{date_start} 6:00 AM', '%d/%m/%Y %I:%M %p')
    d2 = datetime.strptime(f'{date_end} 7:00 PM', '%d/%m/%Y %I:%M %p')
    date_generated = random_date(d1, d2).__format__('%d/%m/%Y %H:%M:%S')
    return date_generated


def data_generator():
    lista_produtos = "Faca Mouse Celular Camiseta Fone Monitor Bermuda Carregador Meia".split()
    lista_fornecedores = "Apple Microsoft Samsung Havan Renner Riachuelo".split()
    # for i in range(15):
    #     date, time = datetime_generator("01/12/2021", "01/03/2022").split()
    #     qtd = randint(1, 30)
    #     custo = randint(1, 20)
    #     margem = 1 + random()
    #     preco_venda = custo * margem
    #     produto = choice(lista_produtos)
    #     fornecedor = choice(lista_fornecedores)
    #     print(
    #         f"{i+1},{produto},{fornecedor},{custo:.2f},{preco_venda:.2f},{qtd},{date},{time}"
    #     )
    for i, fornecedor in enumerate(lista_fornecedores):
        print(
            f"{i + 1},{fornecedor}"
        )


data_generator()
