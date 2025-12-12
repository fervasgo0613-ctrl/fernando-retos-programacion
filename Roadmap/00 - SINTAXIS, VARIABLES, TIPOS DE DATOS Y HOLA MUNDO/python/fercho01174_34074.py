# https://www.python.org

# Esto es un comentario en una linea

x = 10 # Se puede colocar al final de una línea de código para explicarla.

# Se utiliza el símbolo de la almohadilla o numeral (#). El intérprete de Python ignorará todo lo que siga a este símbolo hasta el final de esa línea.

"""
Esto tambien es
un comentario en varias
lineas con 3 comillas dobles antes
del inicio y 3 al cerrar
"""

'''
Esto tambien es
un comentario en varias
lineas con 3 comillas simples antes
del inicio y 3 al cerrar
'''

Mi_variable = "Mi variable"
Edad = 44
Edad = 45 # puedes cambiar su valor en cualquier momento, termina mutando.
Nombre = "Carlos" # puedes cambiar en cualquier momento.

## Constante numerica: el valor de PI
PI = 3.1416     # Al Escribir la variable en MAYUSCULA Indica que el valor asignado a esa variable es fijo y no debe ser modificado durante la ejecución del programa. 
# El intérprete de Python no impedirá que modifiques la variable.
# Al escribir con mayuscala, es por convención.

## Constante de configuracion: un limite maximo
LIMITE_USUARIOS = 500

### datos primitivos

## 1. Cadena de Texto que se encuentra en comillas. (str)
saludo = "Hola, mundo en Python"
mi_nombre_y_apellido = 'Fernando Alexis Vasquez Vasquez' # Se puede usar comillas simples o dobles.
mi_otra_cadena = 'Mi otra Cadena de texto'

## 2. Numerico.
# Entero (int)
cantidad_productos = 150

# Flotante (float). Números decimales negativos o positivos que no este encerrado en comillas. 
temperatura = 36.5
pi_valor = 3.1416

## 3. Booleano (bool)
hay_inventario = True
esta_vacio = False

## 4. Tipo Especial: NodeType
# Aunque no es un primitivo, es fundamental.
valor_nulo = None # Representa la ausencia de valor.

### PRINT
print("¡Hola, Python!")

### Puedes verificar el tipo de cualquier variable utilizando la función type()
print(type(saludo))     # <class 'str'>
print(type(cantidad_productos))     # <class 'int'>
print(type(temperatura))        # <class 'float'>
print(type(hay_inventario))     # <class 'bool'>