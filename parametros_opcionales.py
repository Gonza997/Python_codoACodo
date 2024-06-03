#Funciones
def registrar_datos(nombre, sede = "Buenos Aires", anio = 2024):
    
    print(f"Se ha inscripto a {nombre.title()} en la sede {sede} para el año {anio}") 
    
def datos_sede(direccion, ciudad, provincia = "Buenos Aires"):
    print(f"Universidad de Python - {direccion} - {ciudad} - {provincia}")



#Programa Principal

registrar_datos("agustina gonzález","Córdoba",2021)
registrar_datos("diego lópez","Misiones")
registrar_datos("ANA FERNÁNDEZ")

print(" ")
datos_sede("Av. Las Heras 3456", "Godoy Cruz", "Mendoza")
datos_sede(provincia='Chubut', ciudad='Rawson', direccion='Belgrano 312')
datos_sede(ciudad='Mar del plata', direccion='Av. Moreno 56')
