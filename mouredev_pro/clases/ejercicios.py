#ejercicio
#1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
class Animal:
    def __init__(self,species):
        self.species = species
    def  make_sound(self):
        print("Sonido genércio")

gato = Animal('Gato')
print(gato.species)
gato.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
class Animal:
    def __init__(self, species):
        self.species = species  # Propiedad pública para almacenar la especie
    
    def make_sound(self):
        # Verificamos el sonido según la especie
        if self.species.lower() == "gato":
            print("Miau")
        elif self.species.lower() == "perro":
            print("Guau")
        elif self.species.lower() == "vaca":
            print("Muu")
        else:
            print("Sonido desconocido para esta especie")
# Crear objetos de la clase Animal con diferentes especies
gato = Animal("Gato")
perro = Animal("perro")
print(f"el {gato.species} hace {gato.make_sound()}")           vaca = Animal("vaca")
ave = Animal("ave")

# Probar los sonidos

gato.make_sound()  # Salida: Miau
perro.make_sound()  # Salida: Guau
vaca.make_sound()  # Salida: Muu
ave.make_sound()  

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente sea 0.        
class Car:
     def __init__(self,brand,model):
         self.brand = brand
         self.model = model
         self._spedd = 0
         
# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade tambien un método "brake" que reduzca la velocidad en 10 unidades. Asegurate de que la velocidad no sea negativa.         
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self._speed = 0
    
    def accelerate(self):
        self._speed += 10
    
    def brake(self):
        self._speed = max(0,self._speed -10) 

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el tí­tulo del libro.        
class Book:
    def __init__(self,title,author):
        self.title = title
        self.__author = author
    def get_author(self):
        return self.__author    
                      
    def change_title(self, new_title):
        self.title = new_title             
    
    # 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante. 
   
class Estudiante:
    def __init__(self,nombre,apellido,notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
    def calculate_average(self):
        return sum(self.notas)/ len(self.grades)
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance): 
        self.owner = owner 
        self.balance = balance
    def depossit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Saldo insuficiente")             
    
  # 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5  
    
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.

class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_total_pay(self):
        return self.hourly_wage * self.hours_worked