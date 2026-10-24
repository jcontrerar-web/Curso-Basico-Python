# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        if self.species == "Gato":
            print(f"{self.species} y hace miau")
        elif self.species == "Perro":
            print(f"{self.species} y hace guau")
        else:
            print("Sonido genérico")

my_animal = Animal("Gato")


# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.

"Respuesta en el ejercicio 1."


# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10
        return self.__speed

    def brake(self):
        if self.__speed >= 10:
            self.__speed -= 10
            return self.__speed
        else:
            self.__speed -= 0
            return self.__speed

my_car = Car("Tesla", "Model 3")


# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.

"Respuesta en el ejercicio 3."


# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author

    def change_title(self):
        self.title = input("Escribe el nuevo título")

my_book = Book("Main Kamp", "Hitler")     


# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, name, surname, mark):
        self.mark = mark
        pass

    def media(self):
        for m in self.mark:
            num = sum(self.mark)
            den = len(self.mark)
            media = num / den
            return media
           
student = Estudiante("Javier", "Contreras", [10, 9, 8, 7, 1, 4])


# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        self.balance += int(input("¿Cuánto dineero quieres ingresar en tu cuenta?\n"))
        print (self.balance)

    def retire(self):
        retire = int(input("¿Cuánto dinero quieres retirar de tu cuenta?\n"))
        if self.balance >= retire:
            self.balance -= retire
            print (self.balance)
        else:
            print("No dispones de tantos ingresos")

client = BankAccount("Javier", 1000)


# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5

object = Point(40,30)
print(object.distance(4))


# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def hours_pay(self):
        hours_pay = self.hourly_wage * self.hours_worked
        return hours_pay

empleado = Employee("Javier", 20, 40)


# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self, inventory):
        self.inventory = inventory

    def append(self):
        self.inventory.append(input("Agrega un producto: "))
        for s in self.inventory:
                    print(s)

    def show_inventory(self):
        for product in self.inventory:
            print(product)
        
        
inventario = Store(["Lápiz", "Goma", "Boli"])
        