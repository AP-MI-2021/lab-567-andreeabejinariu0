from Domain.obiect2 import get_object_string, get_name, get_description, get_price, get_location, getNewObject
from Logic.crud import create, read, update, delete
from Logic.mutare import mutare_obiecte_din_locatie
from Logic.concatenare import concatenare_str_dupa_pret_citit
from Logic.cmmpret_locatie import cel_mai_mare_pret_locatie
from Logic.ordonare import ordonare_pret
from Logic.suma import suma_preturi_ptr_locatie


def show_menu():
    print("1. CRUD")
    print("2. Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("3. Concatenarea unui string citit la  descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("4. Determinarea celui mai mare preț pentru fiecare locație.")
    print("5. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("6. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u. Undo")
    print("r. Redo")
    print("x. Iesire")


def handle_add(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului: "))
        nume = input("Dati numele obiectului: ")
        descriere = input("Dati descrierea obiectului: ")
        pret = int(input("Dati pretul de achizitie al obiectului: "))
        locatie = input("Dati locatia obiectului: ")
        return create(obiecte, id_obiect, nume, descriere, pret, locatie)
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_show_all(obiecte):
    for element in obiecte:
        print(get_object_string(element))


def handle_show_details(obiecte):
    id_obiect = int(input("Dati id-ul obiectului pentru care doriti detalii: "))
    obiect = read(obiecte, id_obiect)
    print(f'Nume: {get_name(obiect)}')
    print(f'Descriere: {get_description(obiect)}')
    print(f'Pret:{get_price(obiect)}')
    print(f'Locatie: {get_location(obiect)}')


def handle_update(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului care se actualizeaza: "))
        nume = input("Dati noul numele obiectului: ")
        descriere = input("Dati noua descriere obiectului: ")
        pret = int(input("Dati noul  pretul de achizitie al obiectului: "))
        locatie = input("Dati noua locatia a obiectului: ")
        return update(obiecte, getNewObject(id_obiect, nume, descriere, pret, locatie))
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_delete(obiecte):
    try:
        id_obiect = int(input("Dati id-ul obiectului care se va sterge: "))
        obiecte = delete(obiecte, id_obiect)
        print('Stergerea a fost facuta cu succes')
        return obiecte
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_crud(obiecte):
    while True:
        print("1. Adaugare")
        print("2. Modificare")
        print("3. Stergere")
        print("a. Afisare")
        print("d. Detalii obiect")
        #print("b. Revenire")

        optiune = input("Alege optiunea: ")
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            obiecte = handle_update(obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
        elif optiune == 'a':
            obiecte = handle_show_all(obiecte)
        elif optiune == 'd':
            obiecte == handle_show_details(obiecte)
       #elif optiune == 'b':
       #    return break
        else:
            print("Optiune invalida!")

        return obiecte


def handle_mutare(obiecte):
    try:
        locatie = input("Dati locatia initiala a obiectului: ")
        destinatie = input("Dati destinatia finala a obiectului: ")
        obiecte = mutare_obiecte_din_locatie(obiecte, locatie, destinatie)

        print("Obiectul s-a mutat din locatia initiala in destinatie")

    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_concatenare(obiecte):
    try:
        pret = int(input("Dati pretul unui obiect: "))
        string = input("Dati mesajul care doriti sa se concateneze la descriere: ")
        obiecte = concatenare_str_dupa_pret_citit(obiecte, pret, string)

        print("Concatenarea stringurilor a avut loc")
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_cmmpret_locatie(obiecte):
    try:
        rezultat = cel_mai_mare_pret_locatie(obiecte)
        for locatie in rezultat:
            print("Pentru locatia:{} cel mai mare pret il contine obiectul este"
                  ": {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_ordonare(obiecte):
    try:
        obiecte = ordonare_pret(obiecte)
        print("Ordonarea dupa pretul de achizitie a avut loc")
    except ValueError as ve:
        print('Eroare:', ve)
    return obiecte


def handle_suma(obiecte):
    try:
        rezultat = suma_preturi_ptr_locatie(obiecte)
        for locatie in rezultat:
            print("Pentru locatia:{} suma preturilor este"
                  ": {}".format(locatie, rezultat[locatie]))
    except ValueError as ve:
        print('Eroare: ', ve)

    return obiecte


def handle_new_list(list_versions, current_version, obiecte):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(obiecte)
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


def handle_redo(list_versions, current_version):
    try:
        if current_version >= len(list_versions) - 1:
            print("Nu se mai poate face redo.")
            return list_versions[current_version], current_version
        current_version += 1
        return list_versions[current_version], current_version
    except ValueError as ve:
        print('Eroare: ', ve)


def run_ui(obiecte):
    list_versions = [obiecte]
    current_version = 0

    while True:
        show_menu()
        optiune = input("Optiunea aleasa: ")
        if optiune == '1':
            obiecte = handle_crud(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '2':
            obiecte = handle_mutare(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '3':
            obiecte = handle_concatenare(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '4':
            obiecte = handle_cmmpret_locatie(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '5':
            obiecte = handle_ordonare(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == '6':
            obiecte = handle_suma(obiecte)
            list_versions, current_version = handle_new_list(list_versions, current_version, obiecte)
        elif optiune == 'u':
            obiecte, current_version = handle_undo(list_versions, current_version)
            print('Undo efectuat cu succes!')
        elif optiune == 'r':
            obiecte, current_version = handle_redo(list_versions, current_version)
            print('Redo efectuat cu succes!')
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida!")

    return obiecte
