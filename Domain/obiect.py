
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
    :return: un  dictionar
    '''
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret': _pret,
        'locatie': _locatie
    }
    return obiect


def get_id(obiect):
    return obiect['id']


def get_name(obiect):
    return obiect['nume']


def get_description(obiect):
    return obiect['descriere']


def get_price(obiect):
    return obiect['pret']


def get_location(obiect):
    return obiect['locatie']


def get_object_string(obiect):
    return f'Obiectul cu id-ul {get_id(obiect)} localizat in {get_location(obiect)} si numele {get_name(obiect)}.'
