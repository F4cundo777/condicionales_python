# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

print('Ingrese 3 palabras:')
pal_1 = str(input('Ingrese la primer palabra:\n')).lower()
pal_2 = str(input('Ingrese la segunda palabra:\n')).lower()
pal_3 = str(input('Ingrese la tercer palabra: \n')).lower()
print('eliga entre estas dos opciones para ordenar las palabras')
print('1 - Ordenar por orden alfabético \n2 - Ordenar por cantidad de letras')
opcion = int(input('Ingrese la opcion:\n'))

if opcion==1:
    if pal_1 < pal_2 and pal_1 < pal_3:
        if pal_2 < pal_3:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_1,pal_2,pal_3))
        else:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_1,pal_3,pal_2))
    elif pal_2 < pal_1 and pal_2 < pal_3:
        if pal_1 < pal_3:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_2,pal_1,pal_3))
        else:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_2,pal_3,pal_1))
    elif pal_3 < pal_1 and pal_3 < pal_2:
        if pal_1 < pal_2:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_3,pal_1,pal_2))
        else:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_3,pal_2,pal_1))

else:
    p1_len = len(pal_1)
    p2_len = len(pal_2)
    p3_len = len(pal_3)
    if p1_len < p2_len and p1_len < p3_len:
        if p2_len < p3_len:
             print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_1,pal_2,pal_3))
        else:
             print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_1,pal_3,pal_2))

    elif p2_len < p1_len and p2_len < p3_len:
        if p1_len < p3_len:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_2,pal_1,pal_3))
        else:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_2,pal_3,pal_1))
    elif p3_len < p1_len and p3_len < p2_len:
        if p1_len < p2_len:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_3,pal_1,pal_2))
        else:
            print('Las palabras estan ordenadas de la siguente manera:\n{}\n{}\n{}'.format(pal_3,pal_2,pal_1))

