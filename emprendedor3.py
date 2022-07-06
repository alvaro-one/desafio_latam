#Parte 3
P=float(input("Ingrese el Precio de las suscripciones:"))
U=int(input("Ingrese cantidad de Usuarios:"))
GT=int(input("ingrese Gasto Total:"))
UA= int(input("Ingrese Utilidades del año anterior:"))

utilidad=int(P*U-GT)
print("Las utilidades actuales del proyecto son:",utilidad)
razon=float(utilidad/UA)
print("La razon de las utilidades actuales respecto al año anterior es de:", razon)