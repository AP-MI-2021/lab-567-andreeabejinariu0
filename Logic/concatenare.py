from Domain.obiect2 import get_price, get_description, get_id, get_name, get_location, getNewObject


def concatenare_str_dupa_pret_citit(lista, pret, string):
    '''
    Concatenarea unui string citit de la tastura la descrierea obiectelor cu pretul mai mare decat cel dat
    :param lista: lista obiectelor
    :param pret: pretul citit de la tastatura
    :param string: mesajul care se va concatena la descriere
    :return: lista obiectelor modificata
    '''
    result = []
    descriere = ''
    for element in lista:
        if get_price(element) > pret:
            descriere = get_description(element) + string
            id = get_id(element)
            nume = get_name(element)
            pret = get_price(element)
            locatie = get_location(element)
            obiect = getNewObject(id, nume, descriere, pret, locatie)
            result.append(obiect)

        else:
            result.append(element)

    return result
