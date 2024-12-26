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
vaca = Animal("vaca")
ave = Animal("ave")

# Probar los sonidos
gato.make_sound()  # Salida: Miau
perro.make_sound()  # Salida: Guau
vaca.make_sound()  # Salida: Muu
ave.make_sound()              
print(f"el {gato.species} hace {gato.make_sound()}")           