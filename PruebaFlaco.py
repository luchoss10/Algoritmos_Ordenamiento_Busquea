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


def BubbleSort(vector):
    for i in range(0,len(vector)):
        for j in range(0, len(vector)-1):
            if vector[j]>vector[i]:
                temp=vector[j]
                vector[j]=vector[i]
                vector[i]=temp
                Ic=Ic+1
            Co=Co+1

def Bubble22(vector):
    for i in range(0,len(vector)):
        for j in range(0, len(vector)-1):
            if vector[j]>vector[i]:
                temp=vector[j]
                vector[j]=vector[i]
                vector[i]=temp
            ene = 0


n = int(input())

vec = NVector(n)

BubbleSort(vec)
    