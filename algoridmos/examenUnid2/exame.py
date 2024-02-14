#1.-primer problema
'''Implementa el algoritmo de ordenamiento de selección para ordenar un arreglo de los
números(23, 44, 13, 76,100, 23, 213, 45, 71, 32, 76, 34, 204, 2 ) naturales en orden ascendente.'''
def ordennum(l):
    for i in range(len(l)-1):       
        men = i 
        #se define el numero menor y se guarda
        for j in range(i + 1, len(l)):
            #se compara el nuemro menor con todos los del arreglo
            if l[j] < l[men]:
                men = j
                
        #en caso de que el menor sea diferente de la i se reasigna
        if men != i:
            tem=l[men]
            l[men]=l[i]
            l[i]=tem
            
    
    print(l)


l1=[23, 44, 13, 76,100, 23, 213, 45, 71, 32, 76, 34, 204, 2]
ordennum(l1)

#2.-segundo problema
class produc():
    def __init__(self, nombre, precio):
        self.nombre= nombre
        self.precio=precio
    
'''Implementa un método de 
ordenamiento por inserción para ordenar el arreglo por precio de manera ascendente.'''
def ordenobj(p):
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i].precio > p[j].precio:
                tem=p[i]
                p[i]=p[j]
                p[j]=tem
                
                
    
    for p in p:
        print(f"Nombre: {p.nombre}, Edad: {p.precio}")
    

l2=[
    produc("arina",30),
    produc("agua",30),
    produc("cafe",50)
    ]
ordenobj(l2)

#3.-tercer problema
l3=[8, 23, 12, 25, 65, 45, 50, 99, 90, 13, 16, 71, 32, 49, 83, 65, 67, 38, 18, 1021]
def ordenburbuja(l):
    n = len(l)
    print(f"se define el tamaño del arreglo en la variable {n}")
    for i in range(n):
        for j in range(0, n-i-1):
            
            if l[j] > l[j+1]:
                print(f"se intercambio el {l[j]} por el {l[j+1]}")
                tem=l[j]
                l[j]=l[j+1]
                l[j+1]=tem
                
    
    print(l)
    
ordenburbuja(l3)
#4.-Implementa un método de búsqueda lineal para encontrar 
# la posición de los caracteres vocales del arreglo.
def buslinea(l):
    
    for i in range(len(l)):

        if l[i] =="A" or l[i]=="E" or l[i]=="I" or l[i]=="O" or l[i]=="U":
            
            print(f"vocal {l[i]} encontrada en la pocicion {i}")
    

l4=["D","E","S","A","R", "R", "O","L", "L", "O",  "D", "E",  "S", "O", "F", "T", "W", "A","R","E","T","I"]
buslinea(l4)
#5.- Implementa un método de búsqueda binaria para 
# encontrar la posición de un número específico en el arreglo.
def bus(l, n):
    i = 0
    f = len(l) - 1
    while i <= f:
        m = (i + f) // 2

        if l[m] == n:
            return m
        
        elif l[m] < n:
            i = m + 1
        
        else:
            f = m - 1

    return -1

l5=[1, 2, 3, 4, 5, 6, 7]
print(f"arreglo: {l5}")
n=5
print(f"numero a buscar: {n}")
res = bus(l5,n)
if res != -1:
    print(f"El elemento {n} está en la posición {res}.")
else:
    print(f"El elemento {n} no está en el arreglo.")

#6.-Diseña un escenario de la vida real donde la aplicación de un 
#algoritmo de ordenamiento o búsqueda, puedes tomar como ejemplo cualquiera de los ejemplos visto en clase.

# ecenario ficticio disociativo numero 26
#se busca ordenar un grupo de primaria por calificacion dejando a los que tiene  las calificaciones mas bajas
#en la sona de adelante para lo cual debemos ordenarlas de oforma correcta
def ordencalificacion(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            
            if l[j] > l[j+1]:
                
                tem=l[j]
                l[j]=l[j+1]
                l[j+1]=tem
                
    
    print(l)
l6=[7,10,8,6,7,8,9,9,10,6]
print("orden de las calificaicones")
ordencalificacion(l6)