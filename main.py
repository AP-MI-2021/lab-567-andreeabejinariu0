
from Domain.obiect import getNewObject, get_name, get_object_string
from Logic.crud import create, read, update
lista =[]

lista = create(lista, 1,'birou','primul obiect', 150, 'Cluj')
lista = create(lista, 2, 'hartie', 'bax hartie', 36, 'Floresti')
obiect1= read(lista, 1)

newobject= getNewObject(1, 'birou nou', 'obiect updated ', 150, 'Cluj')
lista = update(lista, newobject)

obiect1= read(lista, 1)

print(obiect1)


# obiect = getNewObject(1,'birou','primul obiect', 150, 'Cluj')
# print(get_object_string(obiect))
