from Domain.obiect2 import get_price


def ordonare_pret(lista):
    '''
    Ordonarea obiectelor crescător după prețul de achiziție
    :param lista:lista obiectelor
    :return:lista ordonata in functie de pret
    '''
    if lista is None:
        raise ValueError(f'Lista este goala')
    return sorted(lista, key=get_price)
