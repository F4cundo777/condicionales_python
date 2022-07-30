# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda



if texto_1 > texto_2:
    print('{} es mayor que {} alfabeticamente'. format (texto_1,texto_2))
elif texto_1 < texto_2:
    print('{} es menor que {} alfabeticamente'. format (texto_1,texto_2))
else:
    print('{} y {} son iguales' .format(texto_1,texto_2))


if len(texto_1) > len(texto_2):
    print('{} tiene mas caracteres que {}' .format(texto_1,texto_2))
elif len(texto_1) < len(texto_2):
    print('{} tiene menos caracteres que {}' .format(texto_1,texto_2))
else:
    print('{} y {} tienen los mismos caracteres' .format(texto_1,texto_2))

if texto_1[0] < texto_2[0]:
    print('{} esta primero en el diccionario que {}'.format(texto_1,texto_2))
elif texto_1[0] > texto_2[0]:
    print('{} esta despues en el diccionario que {}' .format(texto_1,texto_2))
else:
    print('{} y {} comienzan con la misma letra'.format(texto_1,texto_2))


if copia_texto_1 == texto_1:
    print('copia_texto_1 es igual a texto_1')
else:
    print('copia_texto_1 y texto_1 son diferentes')

if copia_texto_1 != texto_2:
    print('copia_texto_1 y texto_2 son diferentes')
else:
    print('copia_texto_1 es igual a texto_2')