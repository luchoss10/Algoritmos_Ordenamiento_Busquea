"""Programa de metodos de ordenamiento"""

import random, sys, time

#Funcion  generar Vector
def NVector(n):
    #Verifica que el valor para generar el vector sea mayor a 0
    if n > 0: 
        #Genera el vector aleatoriamente entre 1000, 9999
        lista = [] # O(1)
        for i in range(0, n): # O(n)
            lista.append(random.randrange(1000,10000)) #O(1)
        return lista # O(1)
    else:
        print("¡No se puede crear un vector de tamaño negativo o 0!")
        sys.exit(True)

#Ordeamiento Burbuja
def OrBurbuja(lista):
    #Se referncia las variables globales para sobreescribir
    global tiempo_burb_final, tiempo_burb_inicio
    #Se toma el tiempo al iniciar el algoritmo de ordenamento
    tiempo_burb_inicio = time.time()
    for i  in range(1,len(lista)):
        for j in range(0,len(lista)-+i):
            if lista[j+1]<lista[j]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    #Se toma el tiempo una vez termino el algoritmo
    tiempo_burb_final = time.time()
    return lista 



print("Prgrama de  metodos de Ordenamiento y Busqueda")
print("Seleccione el metodo de ordenamiento o bsuqueda")


n =  int(input("Ingrese un tamaño para el vector: "))
tiempo_burb_inicio = 0
tiempo_burb_final = 0
vec=NVector(n)
#print(f"El vector es: {vec}")
#print(f"Acomodado es: {OrBurbuja(vec)}") 
vec=OrBurbuja(vec)

print(f"Para un vector de tamaño {n}, el algoritmo se demoro: {tiempo_burb_final-tiempo_burb_inicio} ")
