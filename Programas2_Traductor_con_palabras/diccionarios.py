# DICCIONARIOS (Funcionan como enumeraciones --> NOMBRE:JORGE)

my_diccionario = {'a', 'b'}
print(type(my_diccionario))

my_diccionario = {"Nombre":"Jorge",
                  "Apellido":"Diaz",
                  "Edad":20, 
                  5:"Tmabien sirve con numeros"}
print(type(my_diccionario))

print(my_diccionario[5])

print(my_diccionario.keys())
print(my_diccionario.values())

