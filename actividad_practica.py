# 1) Escribe un programa muestre por pantalla “Hello World”.
"""
print("Hello World")
"""

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
"""
print("El resultado de sumar 3 + 5 es:", 3+5)
"""

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
"""
nombreUsuario = input("Ingrese un nombre: ")
print("Hola", nombreUsuario)
"""

# 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(f"El resultado de sumar {num1} mas {num2} es: {num1+num2}")
"""

# 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if (num1 > num2):
    print(f"El numero mayor es: {num1}")
else:
    print(f"El numero mayor es: {num2}")
"""

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
"""
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if (num1 > num2 and num1 > num3):
    print(f"El numero mayor es: {num1}")
elif (num2 > num1 and num2 > num3):
    print(f"El numero mayor es: {num2}")
else:
    print(f"El numero mayor es: {num3}")
"""

# 7) Escribe un programa que pida un número y diga si es divisible por 2
"""
num = int(input("Ingrese un numero: "))
if (num%2 == 0):
    print(f"El numero {num} es divisible por 2")
else:
    print(f"El numero {num} no es divisible por 2")
"""

# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
"""
num = int(input("Ingrese un numero: "))
if (num%2==0 or num%3==0 or num%5==0 or num%7==0):
    print(f"{num} Es divisible por 2, 3, 5 o 7")
else:
    print(f"{num} No es divisible por 2, 3, 5 o 7")
"""

# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
"""
num = int(input("Ingrese un numero: "))
if (num%2==0 and num%3==0 and num%5==0 and num%7==0):
    print(f"{num} es divisible por 2, 3, 5 y 7")
elif(num%2==0 and num%3==0 and num%5==0):
    print(f"{num} es divisible por 2, 3 y 5")
elif(num%2==0 and num%3==0 and num%7==0):
    print(f"{num} es divisible por 2, 3 y 7")
elif(num%2==0 and num%5==0 and num%7==0):
    print(f"{num} es divisible por 2, 5 y 7")
elif(num%3==0 and num%5==0 and num%7==0):
    print(f"{num} es divisible por 3, 5 y 7")
elif(num%2==0 and num%3==0):
    print(f"{num} es divisible por 2 y 3")
elif(num%2==0 and num%5==0):
    print(f"{num} es divisible por 2 y 5")
elif(num%2==0 and num%7==0):
    print(f"{num} es divisible por 2 y 7")
elif(num%3==0 and num%5==0):
    print(f"{num} es divisible por 3 y 5")
elif(num%3==0 and num%7==0):
    print(f"{num} es divisible por 3 y 7")
elif(num%5==0 and num%7==0):
    print(f"{num} es divisible por 5 y 7")
elif(num%2==0):
    print(f"{num} es divisible por 2")
elif(num%3==0):
    print(f"{num} es divisible por 3")
elif(num%5==0):
    print(f"{num} es divisible por 5")
elif(num%7==0):
    print(f"{num} es divisible por 7")
else:
    print(f"{num} No es divisible por 2, 3, 5 o 7")
"""

# 10) Escribir un programa que escriba en pantalla los divisores de un número dado
"""
num = int(input("Ingrese un numero: "))
if(num<=0):
    print("Ingrese un numero mayor a Cero (0)")
else:
    for i in range(1,11,1):
        if(num>0 and num%i==0):
            print(f"{i} es divisor de {num}")
"""

# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)
"""
numero = int(input("Introduce un número: "))
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
"""

"""
12) Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente"""
"""
nota = int(input("Ingrese la nota: "))
if (nota<=0 or nota>10):
    print("Ingrese un numero del Uno al Diez (1-10)")
elif(nota<3):
    print(f"Nota: {nota} (Muy deficiente)")
elif(nota<=5):
    print(f"Nota: {nota} (Insuficiente)")
elif(nota==6):
    print(f"Nota: {nota} (Suficiente)")
elif(nota<=8):
    print(f"Nota: {nota} (Notable)")
elif(nota<=10):
    print(f"Nota: {nota} (Sobresaliente)")
"""

"""
13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
1
22
333
4444
55555
666666
"""
"""
numero = int(input("numero n: "))
numcol = 0

while numcol < numero:
    fila = numcol + 1
    cont = 0
    m = ""
    while cont < fila:
        m = m + str(numcol + 1) + " "
        cont += 1
    print(m)
    numcol = numcol + 1
"""

"""
14) Haz un programa que escriba una pirámide inversa de los números del 1 al
número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555
4444
333
22
1
"""
'''
numero = int(input("numero n: "))
numcol = 0
while numcol < numero:
    fila = numcol + 1
    cont = 0
    m = ""
    while cont < fila:
        m = m + str(numero - numcol) + " "
        cont += 1
    print(m)
    numcol += 1
'''

'''
15) Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por
ejemplo:
1
2
3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10
'''
'''
for i in range(1,501,1):
    if (i%4==0 and i%9==0):
        print(f"{i} (Multiplo de 4 y de 9)")
        if (i%5==0):
            print("------------------------------------------------------------")
    elif(i%4==0):
        print(f"{i} (Multiplo de 4)")
        if (i%5==0):
            print("------------------------------------------------------------")
    elif(i%9==0):
        print(f"{i} (Multiplo de 9)")
        if (i%5==0):
            print("------------------------------------------------------------")
    else:
        print(f"{i}")
        if (i%5==0):
            print("------------------------------------------------------------")
'''