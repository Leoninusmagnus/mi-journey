# Múltiplos de 3 y 5

Este ejercicio resuelve el problema de encontrar la suma de todos los múltiplos de 3 o 5 menores que 1000. Este problema es equivalente al **Problema 1 de Project Euler**.

## Descripción del Problema
Si enumeramos todos los números naturales menores que 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.

El objetivo es encontrar la suma de todos los múltiplos de 3 o 5 menores que 1000.

## Solución en Python
El script [multiplos_de_3_y_5.py](file:///C:/Users/leoni/.gemini/antigravity/scratch/mi-journey/ejercicios/multiplos_3_y_5/multiplos_de_3_y_5.py) implementa la solución de dos formas:

1. **Método tradicional (Bucle `for`):** 
   Recorre los números del 1 al 999 y acumula la suma de aquellos que son divisibles entre 3 o 5 usando el operador módulo (`%`).
   
2. **Método Pythonico (Comprensión de generadores):**
   Resuelve el problema de manera más compacta y eficiente en una sola línea:
   ```python
   suma_rapida = sum(n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0)
   ```

## Cómo ejecutar el script
Puedes correr el script usando Python en tu terminal:
```bash
python multiplos_de_3_y_5.py
```
