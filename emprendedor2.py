#Parte 2
P=float(input("Ingrese el Precio de las suscripciones:"))
UN=int(input("Ingrese cantidad de Usuarios Normales:"))
UP=int(input("Ingrese cantidad de Usuarios Premium:"))
GT=int(input("ingrese Gasto Total:"))

utilidad=int(P*(UN+UP*1.5)-GT)
print("Las utilidades del proyecto es",utilidad)