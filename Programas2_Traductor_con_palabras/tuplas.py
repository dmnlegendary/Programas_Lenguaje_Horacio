# TUPLAS (Contenido estático)

'''
Funcionan de forma similar a las listas, con la excepcion de que las tuplas no se pueden modificar
'''

my_tupla = (12, "camion", 34.7, True)
print(type(my_tupla))

print(my_tupla[1])
print(my_tupla.count(12)) 
print(my_tupla.index(True)) # Encontrar el dato que nosotros queremos y darnos su posicion

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla = tuple(my_tupla)
print(type(my_tupla))