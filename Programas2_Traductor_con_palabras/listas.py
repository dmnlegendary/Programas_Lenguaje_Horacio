# LISTAS (Puedes modificar su contenido)

my_list = ['Hola', 'Mundo', 'Cosa', 389, 29, False, True, 51.4, 29]
print(type(my_list))

print(my_list)
print(my_list[0]) # Tiene un recorrido de INICIO-FIN
print(my_list[-2]) # Tiene un recorrido de FIN-INICIO

my_list.append("Juan")
print(my_list)

my_list.insert(1, False)
print(my_list)

my_list.remove('Cosa')
print(my_list)

print(my_list.pop(5)) # Devuelve el valor que borro en la posicion 5
print(my_list)

print(my_list.count(29))

my_list.reverse() # Voltea la lista
print(my_list)