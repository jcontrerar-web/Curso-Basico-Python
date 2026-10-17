# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dict = {"Name":"Javier", "Age":33, "Country":"Spain"}
print(type(my_dict))

# 2. Accede al valor de la clave name en el diccionario.

print(my_dict["Name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

my_dict["Job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

my_dict["Age"] = 38
print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del my_dict["Country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

my_other_dict = {1:1, 2:4, 3:9, 4:16, 5:25}
print(my_other_dict)

square = {x:x**2 for x in range(1, 6)} 
print(square)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

my_dict = {"name": "Javier", "age": 37, "country": "Spain"}
print("age" in my_dict)

# 8. Imprime solo las claves del diccionario.

print(my_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

my_list = list(my_dict.keys())
print(my_list)

my_list = my_dict.keys()
print(list(my_list))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys)
print(my_new_dict)