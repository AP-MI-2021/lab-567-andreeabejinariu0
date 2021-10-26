
from Domain.obiect import getNewObject, get_name, get_object_string
from Logic.crud import create, read
lista =[]

lista = create(lista, 1,'birou','primul obiect', 150, 'Cluj')
lista = create(lista, 2, 'hartie', 'bax hartie', 36, 'Floresti')
print(lista)


# obiect = getNewObject(1,'birou','primul obiect', 150, 'Cluj')
# print(get_object_string(obiect))
