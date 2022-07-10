import sys
#Definicion de variables de entrada Nombre de archivo
archivo=sys.argv[1] #Aqui se almacena el nombre archivo txt
with open (f'C:/Users/avill/Desktop/workspace/{archivo}', 'r', encoding="utf-8") as file:
    texto=file.read() #Variable que almacena la lectura del archivo txt

#Definicion de variables para contar caracteres y palabras distintas
cuenta_caracteres = len (set(texto))
cuenta_palabras = len (set(texto.split(" ")))

#Entrega de resultados, los resultados esperados son 40 y 243 respectivamente
print("El número de caracteres distintos es:", cuenta_caracteres)
print("El número de palabras distintas es:", cuenta_palabras)