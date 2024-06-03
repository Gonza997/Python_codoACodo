"""Ejercicio 1: Implementar una clase llamada Estudiante que tendrá como atributos
(variables) su nombre, su apellido, dni y dos métodos (funciones), uno de dichos métodos
inicializará los atributos y el siguiente método los mostrará en pantalla. Definir dos objetos
de la clase Estudiante e incorporar una variable de clase (piernas)."""

#Creamos la clase (sustantivo con la primer letra en mayusculas)
class Estudiante: 
    
    hijos = 2
    #Metodo Constructor
    def inicializar(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        
    
    def imprimir(self):
        print(f"Apellido y Nombre: {self.apellido}, {self.nombre}\nDNI: {self.dni}")
        
        
        
#Programa principal
#Creamos un objeto de la clase Estudiante
estudiante1 = Estudiante()
estudiante1.inicializar("Pepe","Argento", 1321321)
estudiante1.imprimir()

print()
estudiante2= Estudiante()
estudiante2.inicializar("Moni", "Argento", 32165498)
estudiante2.imprimir()

print()
print(f"Los estudiantes tiene {Estudiante.hijos} hijos")
print(f"{estudiante1.nombre} tiene {estudiante1.hijos} hijos")
print(f"{estudiante2.nombre} tiene {estudiante2.hijos} hijos")

print()
estudiante1.hijos = 4
print(f"{estudiante1.nombre} tiene {estudiante1.hijos} hijos")
print(f"{estudiante2.nombre} tiene {estudiante2.hijos} hijos")

print()
estudiante2.edad = 54
print(f"{estudiante2.nombre} tiene {estudiante2.edad} años")
print("="*40)


'''Ejercicio 2: Implementar una nueva clase llamada Estudiante. Esta clase tendrá como
atributos su nombre y su nota. Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje que indique: “Promocionó” (nota >= 7), “Rinde final”
(nota >= 4) o “Desaprobó”.
Definir tres objetos de la clase Alumno, cada uno con una condición de aprobación
distinta.'''

class Alumnos:
    
    #Metodo Constructor
    def inicial(self, nombre_completo, nota):
        
        self.nombre_completo = nombre_completo
        self.nota = nota
        
    
    #Metodo para mostrar los datos
    def imprimir2(self): 
        print(f"Nombre Completo: {self.nombre_completo.title()} - Nota: {self.nota}")
        if self.nota >= 7:
            print("Promociona")
        elif self.nota >=4:
            print("Rinde Final")
        else:
            print("Desaprobó")
            
        print()
        


#Programa Principal
estudiante1 = Alumnos()
estudiante2 = Alumnos()
estudiante3 = Alumnos()
estudiante1.inicial("Juan Serrano", 4)
estudiante2.inicial("Luisa Lopez", 8)
estudiante3.inicial("Romina Perez", 2)

estudiante1.imprimir2()
estudiante2.imprimir2()
estudiante3.imprimir2()
print("="*40)


'''Ejercicio 3: Crear una clase que represente una Materia de la universidad. Definir como
atributos su nombre, carrera, duración en meses y un atributo de clase booleano para
definir que todas las materias no son promocionables. Desarrollar un método __init__
para incializarlos. Crear un método para imprimir los datos del objeto, luego sustituirlo por
el método __str__(). Crear dos objetos. Eliminar uno de ellos a través del método
__del__().'''


class Materia: 
    
    promocionable = False
    #Constructor
    def __init__(self, nombre, carrera, duracion, ):
        self.nombre = nombre
        self.carrera = carrera
        self.duracion = duracion
        
    
    #Metodo para mostrar datos
    def imprimir3(self): 
        print(f"Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuracion: {self.carrera} años\n Promocionalble: {self.promocionable}")
        
    #Metodo para mostrar Datos
    def __str__(self):
        return f"Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuracion: {self.duracion} años\nPromocionalble: {self.promocionable}\n"
        
    
    #Metodo para eliminar el objeto
    def __del__(self):
        print(f"{self.nombre} ha sido eliminado.")
        
        
#Programa Principal
materia1 = Materia("Intro a python", "Sistemas", 6)
print(materia1)

materia2 = Materia("Inteligencia Artificial", "sistemas", 4)
materia2.promocionable = True
print(materia2)
