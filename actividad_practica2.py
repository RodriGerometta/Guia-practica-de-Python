"""
1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. 
No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""

"""
# Declaramos la función
def ingresar_numeros():
    a = int(input("Ingrese el primer numero: "))
    if a < 0:
        print("Ingrese un valor que no sea negativo para el primer numero")
        ingresar_numeros()

    b = int(input("Ingrese el segundo numero: "))
    if b < 0:
        print("Ingrese un valor que no sea negativo para el segundo numero")
        ingresar_numeros()
    c = int(input("Ingrese el tercer numero: "))
    if c < 0:
        print("Ingrese un valor que no sea negativo para el tercer numero")
        ingresar_numeros()

    return a, b, c


def mayor(a, b, c):
    if (a == b):
        print(-1)
    elif(a == c):
        print(-1)
    elif(b==c):
        print(-1)
    else:
        print(max(a, b, c))


# Programa principal
a, b, c = ingresar_numeros()
mayor(a, b, c)
"""

"""
2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según
la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.
"""


# DECLARACION DE FUNCIONES
from datetime import datetime


def validar_fecha(dia, mes, año):
    try:
        fecha = datetime(año, mes, dia)
        return True
    except ValueError:
        return False


def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if validar_fecha(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")


# PROGRAMA PRINCIPAL
main()
