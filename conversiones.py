import sys
#Definicion de variables de entrada
tasa_soles=float(sys.argv[1])
tasa_pesos_argentinos=float(sys.argv[2])
tasa_dolares=float(sys.argv[3])
cantidad_en_clp=float(sys.argv[4])

#Definición de variables de proceso
trans_soles=cantidad_en_clp*tasa_soles
trans_arg=cantidad_en_clp*tasa_pesos_argentinos
trans_dolares=cantidad_en_clp*tasa_dolares

#Entrega de resultados
print(f"Los {cantidad_en_clp} pesos equivalen a:")
print(f"{trans_soles} Soles")
print(f"{trans_arg} Pesos Argentinos")
print(f"{trans_dolares} Dolares")