# * my_vel_filter v1 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d14-EstrDatosFunc-DF-Estructuras2-byCesarAguas-v1/LICENSE)
#  
#
#               Alertas Telematicas
#  Otra solución que se encuentra pendiente es la encargada por una empresa de flotas que
#debe medir mediante telemetría las velocidades de cada una de sus correas
#transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que,
#para poder entregar energía a las correas más lentas, es necesario ralentizar las más
#rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se
#requiere levantar una alerta de la posición de las correas transportadoras que están por
#sobre el promedio.

#Para ello se pide determinar una funcionalidad que calcule el promedio de una lista
#de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta
#con mucha capacidad por lo que se pide no depender de librerías externas.
#Listar las posiciones de todas las correas transportadoras que están sobre el
#promedio.
#Implementar la solución mediante una función en un archivo llamado velocidad.py.
#Se entrega la siguiente lista con una muestra de velocidades para probar las
#funcionalidades.

lst_v = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
            14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 
            14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 
            23, 20, 23, 21]

#   Definiendo funciones necesarias
#
#  Funcion para calcular el promedio de velocidades
def prom_v(velocidades):
    suma = sum(velocidades)
    promedio = suma / len(velocidades)
            #  792  /   60
    return promedio

#   Funcion para determinar si existen velocidades excesivas y si las hay mostrarlas,
#   
def excesos(velocidades):
    promedio = prom_v(velocidades)  # Obtenemos el promedio con la funcion anterior
    #Se reestructura la lista nuevamente con los valores que correspondan.
    excedidas = [i for i, vel in enumerate(velocidades) if vel > promedio]
    return excedidas

    
# Comenzando las rutinas

#Ejecutando funciones y mostrando la lista modificada
excedidas = excesos(lst_v)
print(excedidas)
