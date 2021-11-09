from Domain.obiect2 import get_price, get_location


def cel_mai_mare_pret_locatie(lista):
    '''
    Determinarea celui mai mare preț pentru fiecare locație.
    :param lista:lista obiectelor
    :return: dictionar cu locatiile si pretul de achizitie maxim din fiecare locatie
    '''
    result = {}
    for element in lista:
        locatie = get_location(element)
        pret = get_price(element)
        if locatie in result:
            if pret > result[locatie]:
                result[locatie] = pret
        else:
            result[locatie] = pret

    return result
