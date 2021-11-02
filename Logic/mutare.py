from Domain.obiect2 import get_location, getNewObject, get_name, get_id, get_description, get_price


def mutare_obiecte_din_locatie(lista, locatie, destinatie):
    '''
    Mutarea obiectelor din lista din aceeasi locatie in alta
    :param lista: lista obiectelor
    :param locatie: locatia initiala
    :param destinatie: locatia finala
    :return:lista obiectelor modificata
    '''

    result = []
    for element in lista:
        if get_location(element) != locatie:
            result.append(element)
        else:
            id = get_id(element)
            nume = get_name(element)
            descriere = get_description(element)
            pret = get_price(element)
            obiect = getNewObject(id, nume, descriere, pret, destinatie)
            result.append(obiect)

    return result
