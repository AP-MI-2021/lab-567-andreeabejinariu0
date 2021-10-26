from Domain.obiect import getNewObject, get_id


def create(lista_obiecte: list, _id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    obiect = getNewObject(_id, _nume, _descriere, _pret, _locatie)
    # lista_obiecte.append(obiect)
    # return lista_obiecte
    return lista_obiecte + [obiect]


def read(lista_obiecte: list, id_obiect: int=None):
    obiect_gasit = None

    if id_obiect == None:
        return lista_obiecte

    for obiect in lista_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_gasit = obiect

    return obiect_gasit


def update(lista_obiecte: list, new_object):
    result = []

    for obiect in lista_obiecte:
        if get_id(obiect) == get_id(new_object):
            result.append(new_object)
        else:
            result.append(obiect)

    return result

def delete(lista_obiecte, id_obiect: int):
    result = []

    for obiect in lista_obiecte:
        if get_id(obiect) != id_obiect:
            result.append(obiect)

    return result

