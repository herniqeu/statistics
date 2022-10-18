import math
x = [1.69, 1.62, 1.66, 1.64, 1.81, 1.66, 1.73, 1.69, 1.74, 1.66]
#x = [1,2,3,4,5,5]
#-----------------------------------------------------------------------
def media(x): 
    media = 0
    for i in range(0, len(x)): 
        media += x[i]
    print(media/len(x))
#-----------------------------------------------------------------------
def media2(x): 
    media = 0
    for i in range(0, len(x)): 
        media += x[i]
    return media/len(x)
#-----------------------------------------------------------------------
def moda(x): 
    sum = 0
    lista = []
    for i in range(0,len(x)): 
        lista.append({'posicao':i,'valor':0,'inicial':x[i]})

    for i in range(0, len(x)):
        for j in range(0,len(x)):
            if i != j: 
                if lista[i]['inicial'] == lista[j]['inicial']:
                    lista[i]['valor'] +=1
                    lista[j]['valor'] += 1
    #print(lista)
    print(sortlista(lista)[len(x)-1]['inicial'])
    return sortlista(lista)[0]['inicial']


def sortlista(lista): 
    for i in range(0,(len(x)-1)): 
        for j in range(0,(len(x)-1)):
                if lista[j]['valor'] > lista[j+1]['valor']: 
                    temp = lista[j]['valor']
                    lista[j]['valor'] = lista[j+1]['valor']
                    lista[j+1]['valor'] = temp
    return lista
#-----------------------------------------------------------------------
def variancia(x): 
    sm = 0 
    for i in range(0,len(x)):
        sm += pow(x[i]-media2(x),2)
    variancia = sm/10
    print(variancia)
    return variancia

def variancia2(x): 
    sm = 0 
    for i in range(0,len(x)):
        sm += pow(x[i]-media2(x),2)
    variancia = sm/10
    return variancia
#-----------------------------------------------------------------------
def desvio(x): 
    desvio = pow(variancia2(x), (1/2))
    print(desvio)
    return desvio

def desvio2(x): 
    desvio2  = pow(variancia2(x), (1/2))
    return desvio2
#-----------------------------------------------------------------------
def coeficiente(x): 
    coeficiente = desvio2(x)/(media2(x))
    print(coeficiente)
    return coeficiente
#-----------------------------------------------------------------------
def mediana(x): 
    ordenar(x)
    if len(x) % 2 == 0: 
        k1 = int(len(x)/2)
        k2 = int(len(x)/2)+1
        z = ((x[k1-1]+x[k2-1]))/2
    else:
        z = x[(len(x)+1)/2]
    mediana = z
    print(mediana)
    return mediana
#-----------------------------------------------------------------------
def percentil75(x): 
    ordenar(x)
    percentil75 = x[math.ceil(len(x)*0.75)]
    print(percentil75)
    return percentil75
#-----------------------------------------------------------------------
def percentil25(x): 
    ordenar(x)
    percentil25 = x[math.ceil(len(x)*0.25)]
    print(percentil25)
    return percentil25
#-----------------------------------
def ordenar(x): 
    for i in range(0,len(x)-1): 
        for i in range(0,len(x)-1): 
            if x[i] > x[i+1]: 
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp 
    return x
#-----------------------------------------------------------------------

media(x)
moda(x)
variancia(x)
desvio(x)
coeficiente(x)
mediana(x)
percentil75(x)
percentil25(x)



