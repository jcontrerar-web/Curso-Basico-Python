
# 1. Imprime "Â¡Hola Mundo!" por consola.

print("Hola mundo")

# 2. Escribe un comentario de una sola lÃ­nea explicando quÃ© hace el cÃ³digo del Ejercicio 1.

# El ejercicio 1 muestra en el terminal el "str" que hemos escrito.

# 3. Imprime tu nombre y edad en la misma lÃ­nea utilizando la funciÃ³n print.

print("Me llamo Javi y tengo 33 años")

# 4. Usa la funciÃ³n type() para imprimir el tipo de dato de una cadena de texto, un nÃºmero entero y un nÃºmero decimal.

print(type("Hola Python"))
print(type(33))
print(type(3.14))

# 5. Escribe un comentario en varias lÃ­neas explicando quÃ© son los tipos de datos en Python.

"""Los tipos de datos
son los diferentes parámetros 
con los que vamos a trabajar
como int, float, str, complex..."""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

print("Hola"+" "+"mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma lÃ­nea.

nombre = "Javi"
edad = 33
print(f"{nombre} {edad}")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}")

# 9. Usa print() para mostrar el resultado de la suma de dos nÃºmeros enteros y el tipo de dato resultante.

n = int (input("Introduce un número "))
m = int (input("Introduce otro número "))
z = (n + m)
print(z)
print(type(z))

# 10. Comenta el cÃ³digo del Ejercicio 9, y explica quÃ© hace cada lÃ­nea usando comentarios de una sola lÃ­nea.

# La primer línea obtiene un número, el que introduzcamos, la segunda línea el segundo número.
# Ambos son números enteros, hay que ponerlo así explícitmente porque al intrroducirlo siempre será un str.
# La cuarta línea suma los números introducidos y por último la última línea la imprime.