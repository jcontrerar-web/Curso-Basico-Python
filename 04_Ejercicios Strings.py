# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.

cad1 = "Hola"
cad2 = "Python"
print(cad1, cad2)

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.

cadena = "Esta cadena incluye\nun salto de línea"
print(cadena)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name, surname, age = "Javier", "Contreras", 33
print(f"Me llamo {name} {surname} y mi edad es {age}")
print("Me llamo {} {} y mi edad es {}" .format(name, surname, age))
print("Me llamo %s %s y mi edad es %d" %(name, surname, age))

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.

word = "Python"
a, b, c, d ,e, f = word
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.

word1 = "Programación"
print(word1 [3:7])

text = "Programación"
text_slice = text [3:7]
print(text_slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.

word2 = "Python"
print(word2[::-1])

text2 = "Python"
text2_reversed = text2 [::-1]

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

word3 = "aprendiendo python"
print(word3.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.

word4 = "Progrmación en Python"
print(word4.count("n"))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

cad = "12345"
print(cad.isnumeric())