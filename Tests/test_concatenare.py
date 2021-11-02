from Domain.obiect2 import getNewObject
from Logic.concatenare import concatenare_str_dupa_pret_citit

def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Iasi'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Sala')
    ]

def test_concatenare():
    lista = get_data()
    pret = 100
    string = 'abc'
    lista_noua = concatenare_str_dupa_pret_citit(lista, pret, string)

    assert concatenare_str_dupa_pret_citit(lista, pret, string) == [[1, 'pix', 'desc1', 11, 'Iasi'], [2, 'creion', 'desc 2', 7, 'Arad'], [3, 'birou', 'desc 3abc', 260, 'Cluj'], [4, 'stampila', 'desc 4', 52, 'Cluj'], [5, 'imprimanta', 'desc 5abc', 550, 'Sala']]
    assert len(lista) == len(lista_noua)

test_concatenare()