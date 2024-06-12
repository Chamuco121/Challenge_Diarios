# -*- coding: utf-8 -*-

# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))

# Mostrar la tabla de multiplicar del número dado
print("Tabla de multiplicar del {}:".format(numero))
for i in range(1, 11):
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
