from Domain.obiect2 import get_price, get_location


def suma_preturi_ptr_locatie(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare locație
    :param lista: lista obiectelor
    :return: dictionar cu locatiile si suma preturilor pentru fiecare locatie
    '''
    result = {}
    for element in lista:
        locatie = get_location(element)
        pret = get_price(element)
        if locatie in result:
            result[locatie] = result[locatie] + pret
        else:
            result[locatie] = pret
    return result