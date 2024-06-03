# #Funciones con parametros
# def imprimir_bienvenida(cuat, anio):
#     print("Bienvenidos estudiantes")
#     print(f"{cuat} cuatrimestre {anio}")

# cuat = input("Ingrese un cuatrimestre (1er o 2do): ")
# #Validacion
# while len(cuat) == 0:
#     print("debe ingresar un valor: ")
#     cuat = input("Ingrese un cuatrimestre (1er o 2do): ")    

# anio = int(input("Por favor ingrese el año (mayor a 2000): "))
# #Validacion
# while anio<2000:
#     print("Dato no valido, el año debe ser mayor a 2000")
#     anio = int(input("Por favor ingrese el año (mayor a 2000): "))
    
# imprimir_bienvenida(cuat, anio)



#Funciones
def mostrar_cuotas_curso(importe, forma_pago):
    
    if forma_pago == "CONTADO":
        print(f"forma de pago: Contado. Valor: ${importe-(importe*0.1)}")
    elif forma_pago == "DEBITO" or forma_pago == "DÉBITO": 
        print(f"Forma de Pago: Debito. Valor: ${importe}")
    elif forma_pago == "CREDIO" or forma_pago == "CRÉDITO":
        print("Forma de pago: Credito")
        print("Cuotas\tValor Cuota\tTotal Financiado")
        interes = 1.15
        for i in range(3, 13, 3):
            valor_cuota = importe * interes / i
        total_financiado = valor_cuota * i 
        print(f"{i}\t{valor_cuota}\t{total_financiado}")
        interes = interes + 0.15
    else:
        print("Forma de pago erronea")
        
        
        
        
        
#Ejercicio
importe = float(input("Ingrese un importe: "))
forma_pago = input("Forma de pago(Contado/Debito/Credito): ").upper()

mostrar_cuotas_curso(importe, forma_pago)






