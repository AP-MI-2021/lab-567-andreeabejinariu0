from Domain.obiect2 import get_price


def ordonare_pret(lista):
    if lista is None:
        raise ValueError(f'Lista este goala')
    return sorted(lista, key=get_price)
