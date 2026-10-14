# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.

my_tuple1 = (10, 20, 30, 40, 50)
print(my_tuple1)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.

my_tuple2 = (100, 200, 300, 400, 500)
print(my_tuple2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

my_tuple3 = (1, 2, 3)
#my_tuple3[0] = 10 Error
my_tuple3 = list(my_tuple3)
print(type(my_tuple3))
my_tuple3[0] = 10
print(my_tuple3)
my_tuple3 = tuple(my_tuple3)
print(type(my_tuple3))

# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

my_tuple4 = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple4.count(3))

# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

my_tuple5 = ("Java", "Python", "JavaScript", "Python")
print(my_tuple5.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

my_tuple6 = (1, 2, 3)
my_tuple7 = (4, 5, 6)
my_def_tuple = (my_tuple6 + my_tuple7)
print(my_def_tuple)

# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

my_tuple8 = (10, 20, 30, 40, 50)
my_new_tuple = my_tuple8[2:4]
print(my_new_tuple)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

my_tuple9 = ("rojo", "verde", "azul")
my_tuple9 = list(my_tuple9)
my_tuple9[1] = "Amarillo"
my_tuple9 = tuple(my_tuple9)
print(my_tuple9)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

del my_tuple1
#print(my_tuple1) Error

# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

my_tuple10 = (100,)
my_tuple10 = tuple()
print(type(my_tuple10))

my_tuple10 = (100, )
print(my_tuple10)