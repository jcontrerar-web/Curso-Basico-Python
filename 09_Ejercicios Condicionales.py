# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.

n = int(input("Introduzca un número:\n"))

if n > 0:
    print("Su número es positivo")
elif n == 0:
    print("Su número es 0")
else:
    print("Su número es negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.

age = int(input("Indique su edad:\n"))

if age >= 18:
    print("Enhorabuena, eres myor de edad")
else:
    print("Lo siento, no tienes edad suficiente")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.

string = ""

if string == "":
    print("La cadena de texto está vacía")
else:
    print("La cadena de texto no está vacía")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

n = int(input("Introduzca un número:\n"))
m = int(input("Introduzca otro número:\n"))

if n > m:
    print("El primer número es mayor que el segundo")
elif n < m:
    print("El segundo número es mayor que el primero")
else:
    print("Ambos números son iguales")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.

n = int(input("Introduzaca un número:\n"))

if (n % 3 == 0) and (n % 5 == 0):
    print("Su número es correcto")
else:
    print("Su número es incorrecto")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.

x = int(input("Introduzca un número\n"))

if (x % 2 == 0):
    print("Su núnmero es par")
else:
    print("Su número es impar")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.

age = int(input("Introduzca su edad\n"))

if age >= 18:
    print("Eres mayor de edad, puedes votar")
elif age in range(16, 18):
    print("Puedes votar con un permiso especial")
else:
    print("Eres menor de edad, no puedes votar")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.

password = "Python"
input_password = input("Introduzca su contraseña:\n")

if (password == input_password):
    print("Bienvenido")
else:
    print("¡¡¡ERROR!!!")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).

y = int(input("Introduzca un número\n"))

if y in range(10, 21):
    print("Su número es correcto")
else:
    print("Su número es incorrecto")

# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

color = input("Elija un color entre: rojo, amarillo y verde\n")

if color == "verde":
    print("Puede pasar")
elif color == "amarillo":
    print("Esté alerta")
elif color == "rojo":
    print ("Deténgase")
else:
    print("Su color no es válido")