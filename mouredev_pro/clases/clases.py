#clases
'''
las clases son la base de la creación de objetos y nos perminten estructurar
nuestro codigo de manera mas ordenada y mdoular
Una clase en Python es como un plano o molde para crear objetos. Define
las caracteristicas(atributos) y comportamientos(metodos) de los objetos derivados
de esa clase tendrán. Esto nos permiten trabajar de manera más eficiente con datos complejos
origanzando nuestro codigo en unidades mas manejables. 

'''
### Classes ###

# DefiniciÃ³n

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} Está caminando")


my_person = Person("Antonio", "Heredia")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Antonio", "Heredia", "Heran76")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "ANtonio Heredia Morante(La práctica hace al maestro)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)