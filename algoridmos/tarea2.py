#funcion 
def lista(a,b):
    c=[a,b]
    return c

#Tuplas
def Tuplas(a,b):
    c=(a,b)
    return c

#Diccionarios.
def Diccionarios(a,b):
    c={a:2,b:1}
    return c
#Conjuntos.
def Conjuntos(a,b):
    c={a,b}
    return c

#Estructuras mixtas.
def mix(a,b):
    c = lista(a,Tuplas(a,b))
    return c
#Recursividad.
def recu(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * recu(x-1)

#funcion main
a= "hola"
b="adios"
print(lista(a,b))
print(Tuplas(a,b))
print(Diccionarios(a,b))
print(Conjuntos(a,b))
print(mix(a,b))
print(recu(5))
