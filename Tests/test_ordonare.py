from Domain.obiect2 import getNewObject
from Logic.ordonare import ordonare_pret


def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Iasi'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Iasi')
    ]


def test_ordonare():
    lista = get_data()
    lista_noua = ordonare_pret(lista)
    assert ordonare_pret(lista) == [[2, 'creion', 'desc 2', 7, 'Arad'], [1, 'pix', 'desc1', 11, 'Iasi'], [4, 'stampila', 'desc 4', 52, 'Cluj'], [3, 'birou', 'desc 3', 260, 'Cluj'], [5, 'imprimanta', 'desc 5', 550, 'Iasi']]
    assert len(lista) == len(lista_noua)


test_ordonare()
