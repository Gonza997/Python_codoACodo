# print("===============EDADES============")
# edad = int(input("ingrese una edad mayor a 18 años: "))
# cont_carga_errores = 0 #contador para contar las cargas erroneas que se realizaron

# #validacion
# while edad < 18:
#     cont_carga_errores +=1
#     edad = int(input("Error! Ingrese una edad mayor a 18 años: "))
    
# print(f"La edad ingresada es : {edad}")
# print(f"Se a ingresado {cont_carga_errores} veces la edad incorrecta")


# print("===============PROMEDIOS==============")
# suma = 0
# cant_notas= 0

# for i in range(5):
#     nota = float(input("Ingrese la nota: "))
#     suma += nota
#     cant_notas +=1
    
# promedio = suma / cant_notas
# print(f"El promedio de las notas es {promedio}") 

print("===============INFORME COMEDOR==============")

costo_diario = 1250
print("Dia\tCosto")

for i in range(6): 
    print(i+1, "\t$",(i+1)*costo_diario)
    
    