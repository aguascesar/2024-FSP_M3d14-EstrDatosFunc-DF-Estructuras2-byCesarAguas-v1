# * my_filter v1 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1/LICENSE)
#  
#
#           Filtrado Relevante
#
# La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar
#un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al
#problema. Dada una muestra de los productos que actualmente se encuentran disponibles
#en la tienda (un diccionario), se solicita implementar una función que permita entregar lo
#siguiente:
# 1- Un diccionario con los productos que cumplen una cierta condición dado un umbral
# 2- La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estrictos).
# 3- Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario.

import sys

#   Diccionario anteriormente entregado
precios = {'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}
            

#   Definiendo funciones necesarias
#
#  Funcion para buscar productos que esten dentro de la operacion ya sea mayores que, o menores que.
def filtrar(precios, umbral, operacion='mayor'):
    #  Reestructuramos la lista con los resultados, dependiendo del criterio (mayor o menor)
    if operacion == 'mayor':
        encontrados = {
            producto: 
                precio for producto, precio in precios.items() if precio > umbral
            }
    elif operacion == 'menor':
        encontrados = {
            producto: precio for producto, precio in precios.items() if precio < umbral
            }
    else:
        return "Por favor escriba: python filtro.py [Margen] [mayor/menor]"
    #   Se devuelve la lista modificada.
    return encontrados


    
# Comenzando las rutinas

#Ejecutando funciones y mostrando modificaciones de la lista


if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    filtrados = filtrar(precios, umbral)
    print("Se encontraron los siguientes productos:", ", ".join(filtrados.keys()))

elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    operacion = sys.argv[2]
    filtrados = filtrar(precios, umbral, operacion)
    if isinstance(filtrados, str):
        print(filtrados)
    else:
        print("Se encontraron los siguientes productos:", ", ".join(filtrados.keys()))
else:
    print("Por favor escriba: python filtro.py [Margen] [mayor/menor]")