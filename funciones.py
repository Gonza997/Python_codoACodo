"""Ejercicio 1 (introducción): La universidad desea un programa que permita mostrar a través
de una función un mensaje que permita darle la bienvenida a los alumnos, """

#Funciones - Sintaxis basicas
def imprimir_mensaje():
    print("="*38)
    print("Bienvenidos a la universidad de Python!")
    print("="*38)
    
def imprimir_aulas():
    print("Piso\tAulas")
    for i in range(1, 6):
        print(i, end="\t")
        inicio = i * 100
        fin = inicio + 10
        print(f"{inicio} a {fin}")    

#Programa Principal 
imprimir_mensaje()
print()
imprimir_aulas()




