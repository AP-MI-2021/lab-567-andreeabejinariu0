from Domain.obiect2 import getNewObject, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return[
        getNewObject(1, 'pix', 'desc1', 11, 'Oradea'),
        getNewObject(2, 'creion', 'desc 2', 7, 'Arad'),
        getNewObject(3, 'birou', 'desc 3', 260, 'Cluj'),
        getNewObject(4, 'stampila', 'desc 4', 52, 'Cluj'),
        getNewObject(5, 'imprimanta', 'desc 5', 550, 'Sibiu')
    ]


def test_create():
    lista = get_data()
    new_object = getNewObject(6, 'hartie', 'desc 6', 32, 'Floresti')
    lista_noua = create(lista, 6, 'hartie', 'desc 6', 32, 'Floresti')

    assert len(lista_noua) == len(lista) + 1
    assert new_object in lista_noua


def test_read():
    lista = get_data()
    random_object = lista[2]
    assert read(lista, get_id(random_object)) == random_object
    assert read(lista, None) == lista


def test_update():
    lista = get_data()
    new_object = getNewObject(5, 'hartie', 'desc 6', 32, 'Floresti')
    lista_noua = update(lista, new_object)
    assert len(lista) == len(lista_noua)
    assert new_object in lista_noua
    assert lista[4] != lista_noua[4]


def test_delete():
    lista = get_data()
    delete_id = 3
    deleted_object = read(lista, delete_id)
    lista_noua = delete(lista, delete_id)
    assert len(lista_noua) == len(lista) - 1
    assert deleted_object not in lista_noua


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


test_crud()
