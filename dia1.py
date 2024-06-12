def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        return " "
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])

# ch_inversion_de_cadena.py

# Solicitar la entrada del usuario
cadena_usuario = input("Por favor, ingrese la cadena de caracteres que desea invertir: ")

# Invertir la cadena
cadena_invertida = cadena_usuario[::-1]

# Mostrar la cadena invertida
print(f"La cadena invertida es: {cadena_invertida}")

