import random
'''Ejercicio 5 (colaboración de clases): El comedor de la universidad tiene un sistema de
beneficios a través del cual los alumnos pueden sumar puntos o canjearlos por menús. El
comedor necesita al final del día un reporte de la cantidad de puntos que sus alumnos
poseen. Crear 3 alumnos cuyos atributos son su nombre y la cantidad de puntos que poseen,
inicializado en 0. Crear un método que simule las operaciones de ingresar puntos y de
canjear puntos.'''

class Alumno:
    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        
        
    def __str__(self):
        return f"{self.nombre}\t\t{self.puntos} puntos."
    
    def asignacion_puntos(self, puntos):
        self.puntos += puntos
        
    def canjear_puntos(self, puntos): 
        self.puntos -= puntos
        
    def retornar_puntos(self): 
        return self.puntos

#Clase comedor que se va a encargar de crear los objetos y realizar los movimientos    
class Comedor: 
    #Constructor
    def __init__(self, nombre_sede):
        self.nombre_sede = nombre_sede
        self.alumno1 = Alumno("Juan")
        self.alumno2 = Alumno("Luciana")
        self.alumno3 = Alumno("Roxana")
        
    def __str__(self):
        return f"{'='*30}\n{self.nombre_sede}\n{'='*30}"
    
    #Simula movimientos
    def operaciones(self):
        self.alumno1.asignacion_puntos(100)
        self.alumno2.asignacion_puntos(150)
        self.alumno3.asignacion_puntos(300)
        self.alumno1.asignacion_puntos(150)
        
        self.alumno1.canjear_puntos(200)
        self.alumno1.canjear_puntos(150)
        
    def puntos_totales(self): 
        print(f"Detalle de puntos: ")
        print(self.alumno1)
        print(self.alumno2)
        print(self.alumno3)
        print("-"*30)
        total = self.alumno1.retornar_puntos() + self.alumno2.retornar_puntos() + self.alumno3.retornar_puntos()
        print(f"Total: {total} puntos.")
        
        
#Programa Principal
comedor1 = Comedor("El comedor de la Universidad")
print(comedor1)
comedor1.operaciones()
comedor1.puntos_totales()



class Dado:
    def tirar(self): 
        self.valor = random.randint(1, 6)
        
    def imprimir(self): 
        print(f"{self.valor}", end=" ")
        
    
class JuegoDeDados: 
    
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()
    
    def Jugar(self): 
        self.dado1.tirar()
        self.dado1.imprimir()
        
        self.dado2.tirar()
        self.dado2.imprimir()
        
        self.dado3.tirar()
        self.dado3.imprimir()
        
        valor_dado1= self.dado1.valor
        valor_dado2= self.dado2.valor
        valor_dado3= self.dado3.valor
        
        if valor_dado1 == valor_dado2 and valor_dado1 == valor_dado3: 
            print("Ganaste")
        else: 
            print("Perdiste")
            
    def simular_jugadas(self, cantidad): 
        self.cantidad = cantidad
            
        for i in range(1, cantidad):
            self.Jugar()
                
jugada = JuegoDeDados()
jugada.simular_jugadas(20)
        