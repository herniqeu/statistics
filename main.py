import math
#x = [1.69, 1.62, 1.66, 1.64, 1.81, 1.66, 1.73, 1.69, 1.74, 1.66]
x = [1,2,3,4,5,5]
#-----------------------------------------------------------------------
def media(x): 
    media = 0
    for i in range(0, len(x)): 
        media += x[i]
    media = media/len(x)
    return media
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
    return sortlista(lista)[0]['inicial']
#-----------------------------------------------------------------------
def variancia(x): 
    sm = 0 
    for i in range(0,len(x)):
        sm += pow(x[i]-media(x),2)
    variancia = sm/10
    return variancia
#-----------------------------------------------------------------------
def desvio(x): 
    desvio = pow(variancia(x), (1/2))
    return desvio
#-----------------------------------------------------------------------
def coeficiente(x): 
    coeficiente = (desvio(x))/(media(x)) * 100
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
    return mediana
#-----------------------------------------------------------------------
def percentil75(x): 
    ordenar(x)
    percentil75 = x[math.ceil(len(x)*0.75)]
    return percentil75
#-----------------------------------------------------------------------
def percentil25(x): 
    ordenar(x)
    percentil25 = x[math.ceil(len(x)*0.25)]
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

def sortlista(lista): 
    for i in range(0,(len(x)-1)): 
        for j in range(0,(len(x)-1)):
                if lista[j]['valor'] > lista[j+1]['valor']: 
                    temp = lista[j]['valor']
                    lista[j]['valor'] = lista[j+1]['valor']
                    lista[j+1]['valor'] = temp
    return lista
#-----------------------------------------------------------------------

media1 = media(x)
moda1 = moda(x)
desvio1 = desvio(x)
coeficiente1 = coeficiente(x)
mediana1 = mediana(x)
percentil751 = percentil75(x)
percentil251 = percentil25(x)

print(f"A média é : {media1}\n")
print(f"A moda é : {moda1}\n")
print(f"O desvio é : {coeficiente1}\n")
print(f"A mediana é : {mediana1}\n")
print(f"O percentil 75 é : {percentil751}\n")
print(f"O percentil 25 é : {percentil251}\n")

