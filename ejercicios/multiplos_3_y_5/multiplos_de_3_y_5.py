# INICIO

# inicializar suma = 0
suma = 0

# PARA cada número n desde 1 hasta 999:
# Nota: En Python, range(1, 1000) llega hasta el 999.
for n in range(1, 1000):
    
    # SI n es divisible entre 3 O n es divisible entre 5 ENTONCES
    # El operador % (módulo) calcula el resto de la división. 
    # Si el resto es 0, es porque es divisible.
    if n % 3 == 0 or n % 5 == 0:
        
        # suma = suma + n
        suma = suma + n
        
    # FIN SI
# FIN PARA

# mostrar suma
print("La suma de todos los múltiplos de 3 o 5 menores a 1000 es:")
print(suma)

# FIN


# ---------------------------------------------------------
# EXTRA: La forma "Pythonica" (más corta) de hacer lo mismo
# ---------------------------------------------------------
# Python permite comprimir este mismo bucle en una sola línea 
# usando lo que se conoce como "comprensión de generadores":
#
# suma_rapida = sum(n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0)
# print(f"Resultado usando método corto: {suma_rapida}")
