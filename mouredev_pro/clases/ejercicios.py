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
                 