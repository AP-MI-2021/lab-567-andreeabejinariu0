from Domain.obiect2 import getNewObject
from Logic.mutare import mutare_obiecte_din_locatie


def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Iasi'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Sala')
    ]


def test_mutare():
    lista = get_data()
    locatie = 'Arad'
    destinatie = 'Sala'
    lista_noua = mutare_obiecte_din_locatie(lista, locatie, destinatie)
    assert mutare_obiecte_din_locatie(lista, locatie, destinatie) == [[1, 'pix', 'desc1', 11, 'Iasi'], [2, 'creion', 'desc 2', 7, 'Sala'], [3, 'birou', 'desc 3', 260, 'Cluj'], [4, 'stampila', 'desc 4', 52, 'Cluj'], [5, 'imprimanta', 'desc 5', 550, 'Sala']]
    assert len(lista) == len(lista_noua)


test_mutare()
