# SETS (Modificables, pero sin orden y no pueden albergar un mismo dato en dos espacios)

my_set = {"Python", "JavaScript", "C++"}
print(type(my_set))

# print(my_set[0]) TypeError: 'set' object is not subscriptable

my_set.add('C++')
print(my_set)

my_set.add('C#')
print(my_set)

my_set0 = {"Python", "JavaScript", "C++"}

my_set.difference_update(my_set0) # Funciona como resta de información
print(my_set)