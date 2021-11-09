from Logic.cmmpret_locatie import cel_mai_mare_pret_locatie
from Domain.obiect2 import getNewObject

def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Iasi'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Iasi')
    ]


def test_cmmmpret_locatie():
    lista = get_data()
    lista_noua = cel_mai_mare_pret_locatie(lista)
    assert cel_mai_mare_pret_locatie(lista) == {'Iasi': 550, 'Arad': 7, 'Cluj': 260}
    assert len(lista) != len(lista_noua)


test_cmmmpret_locatie()