from Domain.obiect2 import getNewObject
from Logic.suma import suma_preturi_ptr_locatie

def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Iasi'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Iasi')
    ]

def test_suma():
    lista = get_data()
    lista_noua = suma_preturi_ptr_locatie(lista)
    assert suma_preturi_ptr_locatie(lista) == {'Iasi': 561, 'Arad': 7, 'Cluj': 312}
    assert len(lista) != len(lista_noua)

test_suma()