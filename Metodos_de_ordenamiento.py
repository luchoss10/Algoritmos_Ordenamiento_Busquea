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
def OrdBurbuja(lista):
    #Se referncia las variables globales para sobreescribir
    global tiempo_final, tiempo_inicio
    #Se toma el tiempo al iniciar el algoritmo de ordenamento
    tiempo_inicio = time.time()
    for i  in range(1,len(lista)):
        for j in range(0,len(lista)-+i):
            if lista[j+1]<lista[j]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    #Se toma el tiempo una vez termino el algoritmo
    tiempo_final = time.time()
    return lista 

#Ordenamiento Por Insercion
def OrdInserc(A):
    for i in range(len(A)):
        for j in range(i,0,-1):
            if(A[j-1] > A[j]):
                aux=A[j]
                A[j]=A[j-1]
                A[j-1]=aux
    print(A)

#Ordenamiento QuickSort
def OrdQuickSort(lista):
    global tiempo_final, tiempo_inicio
    tiempo_inicio = time.time()
    
    if len(lista) <= 1:
        return lista
        
    derecha = []
    izquierda = []
    medio = []
    pivote = lista[0]
    medio.append(pivote)

    for i  in range(1,len(lista)):
        if lista[i] < pivote:
            izquierda.append(lista[i])

        else:
            derecha.append(lista[i])
    #print(f"{izquierda } - {pivote} - {derecha}")

    return OrdQuickSort(izquierda) + medio + OrdQuickSort(derecha)

def BusSecuen(lista, eval):
    n=0
    while n < len(lista):
        if eval == lista[n]:
            return n
        n += 1
    
    return -1

def BusBinaria(lista, eval):
    inf = 0
    sup = len(lista) - 1
    while inf <= sup:
        mit =  inf+sup//2
        if lista[mit] == eval:
            return mit
        elif eval < lista[mit]:
            sup = mit - 1
        else:
            inf = mit + 1
    
    return -1

print("Programa de  metodos de Ordenamiento y Busqueda")
print("Seleccione el metodo de ordenamiento o bsuqueda")


n =  int(input("Ingrese un tamaño para el vector: "))
tiempo_inicio = 0
tiempo_final = 0
vec=NVector(n)
OrdInserc(vec)

#print(f"El vector es: {vec}")
#print(f"Acomodado es: {OrdBurbuja(vec)}") 
#vec=OrdBurbuja(vec)
#vecOrd =  OrdQuickSort(vec)
#tiempo_final = time.time()
#print(vecOrd)
#print(f"Para un vector de tamaño {n}, el algoritmo se demoro: {tiempo_final-tiempo_inicio} ")


arreglo_1 = [0,5,7,8,4,6,9,10,11,2,3,1,20]
arreglo_2 = [15,17,18,19,20,35,1085,71,23,54]
#ar = OrdQuickSort(arreglo_2)
#           [0 1 2 3 4 5 6  7  8 9 10 11 12]
#i = int(input("Ingrese el elemento a buscar: "))
#valor = BusSecuen(arreglo, i) 
#valor = BusBinaria(ar, i)
#print(arreglo_2)
#print(ar)


# if valor >= 0:
#     print(F"El elemento: {i} se encuentra en la posicion {valor}")
# else:
#     print(F"El elemento: {i} no se encuentra en la lista")
    

