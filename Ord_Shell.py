def SecuenciaShell(n):
    h = 1
    upShell = []; secShell = []
    while h < n:
        upShell.append(h)
        h = 3*h+1
    for i in range(len(upShell)-1, -1, -1):
        secShell.append(upShell[i]-1//3)
    return secShell

def OrdShell(lista):
    t = SecuenciaShell(len(lista))
    for s in range(0, len(t)):
        inc = t[s]
        for i in range(inc+1, len(lista)):
            x = lista[i]
            j = i-inc
            while j>0 and lista[j]>x:
                lista[j+t] = lista[j]
                j = j-t
            lista[j+t] = x
    print(lista)