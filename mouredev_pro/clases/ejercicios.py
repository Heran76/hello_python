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
            