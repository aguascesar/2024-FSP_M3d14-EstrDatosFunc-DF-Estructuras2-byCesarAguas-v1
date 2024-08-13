# * my_factorial_calc v1 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1/LICENSE)
#  
#
#               Apoyo matemático. 
#Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda
#escolar que tiene la esta ONG se está enseñando a programar algunas operaciones
#avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos
#operaciones conocidas como el factorial y la productoria y se requiere que usted prepare
#una script que implemente esto.

#   Definiendo funciones necesarias
#
#  Funcion para calcular el numero factorial de n (numero entero)
def factorial(n):
    f_n = 1
    for i in range(1, n + 1):
        f_n *= i
    return f_n

#   Funcion extraer la productoria desde una lista
def productoria(lst):
    p_l = 1
    for num in lst:
        p_l *= num
    return p_l

#   Esta funcion permite realizar las funciones anteriormente declaradas,
#en el orden que se especifica a continuacion.
def calcular(**kwargs):
    #   Se utiliza la norma de diccionarios,
    # clave, valor dentro de los parametros pasados como argumentos.
    for key, value in kwargs.items():
        #   Comenzamos buscando las claves (cadenas) 
        # Si la cadena es "fn", 
        if key.startswith("fn"):
            #   Se toma el valor que sirve como argumento para la funcion "factorial",
            #y se guarda el resultado.
            resultado = factorial(value)
            print(f"El factorial de {value} es {resultado}")
        # En caso de que la cadena sea "prod"
        elif key.startswith("pl"):
            #   Se toma el valor que sirve como argumento para la funcion "productoria",
            #y se guarda el resultado.
            resultado = productoria(value)
            print(f"La productoria de {value} es {resultado}")



# Comenzando las rutinas

#   Ejecutando funciones y mostrando la lista modificada, en el orden especifico.
#En este caso:
#funcion(factorial de 5, productoria de la lista[4, 6, 7, 4, 3], factorial de 6)
calcular(fn_1=5, pl=[4, 6, 7, 4, 3], fn_2=6)