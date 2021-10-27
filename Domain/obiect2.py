
lista_obiecte = []


def get_all_object():
    return lista_obiecte


def getNewObject(_id: int, _nume: str, _descriere: str, _pret: int, _locatie: str):
    '''
    :param _id: int
    :param _nume: string
    :param _descriere: string
    :param _pret: int
    :param _locatie: string
    :return: o lista
    '''

    obiect = [_id, _nume, _descriere, _pret, _locatie]

    return obiect


def get_id(obiect):
    return obiect[0]


def get_name(obiect):
    return obiect[1]


def get_description(obiect):
    return obiect[2]


def get_price(obiect):
    return obiect[3]


def get_location(obiect):
    return obiect[4]


def get_object_string(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)} localizat in {get_location(obiect)} si numele {get_name(obiect)}.'
