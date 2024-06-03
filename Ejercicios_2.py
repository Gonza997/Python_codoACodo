import datetime
# A) DNI: debe tener solamente numeros
dni = input("ingrese su DNI: ")

#Validacion 
while not dni.isdigit(): 
    dni = input("Error, debe contener solo numero. Por favot ingrese su DNI: ")
    
#B) no debe tener mas de 30 caracteres 
nombre = input("ingrese su nombre: ")

#Validacion
while len(nombre) > 30: 
    nombre = input("Error, el nombre ingresado supera la cantidad de caracteres (30) permitidos, ingrese nuevamente su nombre: ")
    
#C)El apellido debe contener solamente letras
apellido = input("Ingrese su apellido: ")

#Validacion 
while not apellido.isalpha():
    apellido = input("Error, por favor ingrese su apellido: ")
    
#D) El domicilio puede tner letras y numeros, pero debe tener al menos un numero
domicilio = input("Ingrese su domicilio: ")

digitos = 0

for i in domicilio: 
    if i.isdigit():
        digitos +=1
        

#Validacion 

while digitos==0:
    domicilio = input("Error! Ingrese su domicilio: ")
    for i in domicilio:
        if i.isdigit():
            digitos +=1
            
            
# # Obtener la fecha y hora actual
# ahora = datetime.datetime.now()

# # Formatear la fecha en el formato deseado
# fecha_formateada = ahora.strftime("%d/%m/%Y")

# # Imprimir la fecha
# print(f"Fecha actual (día/mes/año): {fecha_formateada}")


#E) Muestra de datos 
ahora = datetime.datetime.now() 

fecha = ahora.strftime("%d/%m/%Y").rjust(56)

linea = "="*56
encabezado = " Univerdidad de python - datos del estudiante "
titulo_centrado = encabezado.center(56, "=")
titulo = titulo_centrado.title()

print(fecha)
print(linea)
print(titulo)
print(linea)

id_usuario = dni.zfill(11)#relleno hasta llegar 11 digitos con ceros
print(f"DNI: {id_usuario}")
print(f"Nombre completo: {apellido.upper()}, {nombre.title()}")
print(f"Domicilio: {domicilio.upper()}")
print(f"Usuario: {apellido.lower()}-{nombre[0].lower()}{dni[:3]}")
nombres = nombre.split(" ")
print(f"Correo Electronico: {apellido.lower()}.{nombres[0].lower()}@unipython.com.ar")
print(f"Contraseña: {apellido[0].upper()}{nombre[0].lower()}-{dni[-3:]}")
print()
leyenda = '''recomendamos cambiar su contraseña.
nose que mas 
nose que mas'''
print(leyenda)

