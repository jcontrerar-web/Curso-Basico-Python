# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.

number = 1
while number in range(1, 11):
    print(number)
    number += 1
else:
    print("Tu número se salió de rango")

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print(element)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.

n = 1
acum = 0

while n <= 100:
    acum = acum + n
    n += 1
    print(acum)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".

word = "Python"

for element in word:
    print(element)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.

n = 1

while (n in range(1, 50)):
    if n % 7 != 0:
        print(f"{n} no es el número que buscamos")
    else:
        print(f"{n} es divisibles entre 7")
        break
    n += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

my_dict = {"name" : "Javier", "age": 33, "country": "Spain"}

for element in my_dict:
    print(element)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.

n = 1

while (n in range (1, 21)):
    if n % 2 == 0:
        print(f"{n} es un número par")
    else:
        print(f"{n} no es un número par")
    n += 1
    
# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

my_list = range(10, 0, -1)

for n in my_list:
    print(n)

for n in range(10, 0, -1):
    print(n)

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].

my_list = [30, 10, 30, 20, 30, 40]

for n in my_list:
    print(my_list.count(30))

counter = 0

for n in my_list:
    if n == 30:
        counter += 1
print(counter)     

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

nombres = ["javi", "ivan", "cesar", "yuri", "brais", "jorge"]

for nombre in nombres:
    if nombre == "brais":
        print(nombre)
        break