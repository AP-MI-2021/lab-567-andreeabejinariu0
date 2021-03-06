
from Domain.obiect2 import getNewObject
from Logic.mutare import mutare_obiecte_din_locatie
from Logic.concatenare import concatenare_str_dupa_pret_citit
from Logic.crud import create, read, update, delete
from Logic.cmmpret_locatie import cel_mai_mare_pret_locatie
from Logic.ordonare import ordonare_pret
from Logic.suma import suma_preturi_ptr_locatie


def handle_add(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        return create(lista, id, nume, descriere, pret_achizitie, locatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_read(lista, lista_date):
    try:
        read_id = int(lista_date[1])
        if read(lista, read_id) is None:
            return 'Id-ul citit nu corespunde vreunui element din lista!'
        else:
            return read(lista, read_id)
    except ValueError as ve:
        print('Eroare: ', ve)
    return []


def handle_update(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        update_obiect = getNewObject(id, nume, descriere, pret_achizitie, locatie)
        update_list = update(lista, update_obiect)
        return update_list
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_delete(lista, lista_date):
    try:
        delete_id = int(lista_date[1])
        new_list = delete(lista, delete_id)
        return new_list
    except ValueError as ve:
        print('Eroare:', ve)
    except TypeError as te:
        print('Eroare:', te)
    return lista


def showmenu():
    print('1.Adaugarea unui obiect in lista')
    print('2.Afisarea unui obiect cu id-ul dat de la tastatura')
    print('3.Modificarea unui obiect din lista, care are acelasi id cu un nou obiect dat de la tastatura')
    print('4.Stergerea unui obiect cu id-ul dat de la tastatura')
    print('5.Mutarea unor obiecte dintr-o locatie in alta')
    print('6.Concatenarea unui string citit la toate descrierile obiectelor cu pre??ul mai mare dec??t o valoare citit??.')
    print('7.Determinarea celui mai mare pre?? pentru fiecare loca??ie.')
    print('8.Ordonarea obiectelor cresc??tor dup?? pre??ul de achizi??ie.')
    print('9.Afi??area sumelor pre??urilor pentru fiecare loca??ie.')
    print("u. Undo")
    print("r. Redo")
    print('a.Afisarea listei de obiecte')
    print('x.Iesire')


def help():
    print('Cum poti accesa o comanda: ')
    print('1. - exemplu : 1,id(int),nume(str),descriere(str),pret_achizitie(int),locatie(str)')
    print('2. - exemplu : 2,id(int)')
    print('3. - exemplu : 3,id(int),nume(str),descriere(str),pret_achizitie(int),locatie(str)')
    print('4. - exemplu : 4,id(int)')
    print('5. - exemplu : 5,locatie(str-locatia de unde vrem sa mutam),destinatie(str-locatia unde vrem sa mutam)')
    print('6. - exemplu : 6,string(str- stringul pe care dorim sa il adaugam),pret(int-pretul cu care vom compara)')
    print('7. - exemplu : 7')
    print('8. - exemplu : 8')
    print('9. - exemplu : 9')
    print('u. - exemplu : u')
    print('r. - exemplu : r')
    print('a. - exemplu : a')
    print('x. - exemplu : x')
    print('Dati comenzile urmate de datele aferente dupa modelul de mai sus separate prin ";"!')
    print('Exemplu: 2,3;a;4,1')
    print('Exemplu: 2,4;a;8;a')
    #print('Exemplu: 6,'as',50;a')
    #print('Exemplu: 1,5,'masa','desc5',59,'ARAD';2,3;a')


def handle_change_location(lista, lista_date):
    try:
        locatie = lista_date[1]
        destinatie = lista_date[2]
        return mutare_obiecte_din_locatie(lista, locatie, destinatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_concatenare(lista, lista_date):
    try:
        string_citit = lista_date[1]
        pret = int(lista_date[2])
        return concatenare_str_dupa_pret_citit(lista, string_citit, pret)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_cmmpret_locatie(lista):
    try:
        rezultat = cel_mai_mare_pret_locatie(lista)
        for locatie in rezultat:
            print("Pentru locatia:{} cel mai mare pret il contine obiectul este"
                  ": {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_ordonare(lista):
    try:
        lista = ordonare_pret(lista)
        print("Ordonarea dupa pretul de achizitie a avut loc")
    except ValueError as ve:
        print('Eroare:', ve)
    return lista


def handle_suma(lista):
    try:
        rezultat = suma_preturi_ptr_locatie(lista)
        for locatie in rezultat:
            print("Pentru locatia:{} suma preturilor este"
                  ": {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare: ', ve)

    return lista


def handle_new_list(list_versions, current_version, lista):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(lista)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    if current_version < 1:
        print("Nu se mai poate face undo.")
        return [], 0
    else:
        print("Undo efectuat cu succes!")
    current_version -= 1
    return list_versions[current_version], current_version


def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        print("Nu se mai poate face redo.")
        return list_versions[current_version], current_version
    else:
        print('Redo efectuat cu succes!')
    current_version += 1
    return list_versions[current_version], current_version


def header(lista):
    list_versions = [lista]
    current_version = 0

    while True:
        showmenu()
        help()
        obtiuni = input('Dati sirul de obtiuni si date: ')
        lista_obtiune = obtiuni.split(sep=';')
        for element in lista_obtiune:
            lista_date = element.split(sep=',')
            obtiune = lista_date[0]
            if obtiune == '1':
                lista = handle_add(lista, lista_date)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '2':
                print(handle_read(lista, lista_date))
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '3':
                lista = handle_update(lista, lista_date)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '4':
                lista = handle_delete(lista, lista_date)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '5':
                lista = handle_change_location(lista, lista_date)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '6':
                lista = handle_concatenare(lista, lista_date)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '7':
                lista = handle_cmmpret_locatie(lista)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '8':
                lista = handle_ordonare(lista)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == '9':
                lista = handle_suma(lista)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == 'a':
                print(lista)
                list_versions, current_version = handle_new_list(list_versions, current_version, lista)
            elif obtiune == 'u':
                lista, current_version = handle_undo(list_versions, current_version)
            elif obtiune == 'r':
                lista, current_version = handle_redo(list_versions, current_version)
            elif obtiune == 'x':
                break
            else:
                print('Obtiune invalida! Incearca altceva!')
        break

    return lista
