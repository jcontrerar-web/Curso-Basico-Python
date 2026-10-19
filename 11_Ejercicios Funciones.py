# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting(name = "desconocido"):
    print(f"Hola, {name}")

personalized_greeting("javier")


# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(num1, num2):
    sum = num1 * num2
    return sum

result = multiply(2, 3)
print(result)

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(148392))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.

def convert_to_uppercase(code):
    return code.upper()

print(convert_to_uppercase("javier"))

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*num):
    result = sum(num)
    return result

print(arbitrary_sum(1, 2, 3, 4, 5, 6))


# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(name, surname):
    return print(f"Hola, {name} {surname}")

generate_full_greeting(surname = "Contreras", name ="Javier")

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(base, exp):
    result = base ** exp
    return result

total = power(2, 9)
print(total)

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.

def calculate_average(num1, num2, num3):
    prom = (num1 + num2 + num3) / 3
    return prom

result = calculate_average(2, 4, 8)
print(result)

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.

def count_characters(cad):
    return len(cad)

result = count_characters("javier")
print(result)

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*cads):
    for cad in cads:
        print(cad.upper())

display_messages("javier", "contreras", "rodriguez")