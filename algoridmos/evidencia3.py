'''
Cálculo del Máximo Común Divisor (MCD) (5%)
Descripción del problema: Crea una clase CalculadoraRecursiva que 
tenga un método llamado calcular_mcd que reciba dos números y 
devuelva el Máximo Común Divisor (MCD) utilizando el algoritmo de Euclides de forma recursiva.
'''
def limpia(a):
    i=0
    while a>1:
        a-=1
        i+=1
    
    return i

def calcular_mcd(a,b):
    if a>b:
        print("a mayor")
        if (a/b)%2==0:
            print("no residuo")
            print("a es "+str(a)+" y b es "+str(b))
            c=a/b
            print(c)
            return c
        else:
            print("residuo " + str(a/b))
            c=b*(limpia(a/b))
            c=a-c
            print(c)
            return calcular_mcd(b,c)
    else:
        print("b mayor")
        if (b/a)%2==0:
            print("no residuo")
            print("a es "+str(a)+" y b es "+str(b))
            c=b/a
            return c
        else:
            print("residuo " + str(a/b))
            c=a*(limpia(b/a))
            c=b-c
            print(c)
            return calcular_mcd(a,c)
'''
   Suma de Dígitos (5%)
Descripción del problema: Implementa un método suma_digitos en la clase CalculadoraRecursiva 
que reciba un número entero y devuelva la suma de sus dígitos de manera recursiva.     
'''
def suma_digitos(u):
    n=1
    while u>n:
        n*=10
        
    n/=10
    if u<10:
        print("la suma total fue "+str(u))
        return limpia(u)
    else:
        c=u/n 
        u+=limpia(c)
        n*=limpia(c)
        u-=n
        suma_digitos(u)
        
    '''
    Descripción del problema: Extiende la clase CalculadoraRecursiva con un método llamado 
    generar_fibonacci que reciba un número �n y devuelva los primeros �
       n términos de la secuencia de Fibonacci de manera recursiva.
    '''
def generar_fibonacci(n):
    if n>0:
        a=0
    b=1
    c=0
    i=0
    while i<n:
        c=a+b
        if i>0:
            if i== n-1:
                print(i,".-",c)
                generar_fibonacci(n-1)
        i+=1
        b=a
        a=c
    else:
        return 0;
    
        
        
        
'''
Potencia Recursiva (5%)
Descripción del problema: Añade un método
potencia_recursiva a la clase CalculadoraRecursiva que reciba dos números, 
base y exponente, y devuelva 
baseexponente de manera recursiva.
'''
def potencia_recursiva(b,e):
    if e<2:
        return b
    else:
        e-=1
        print(e)
        return (b *potencia_recursiva(b,e) )
    
'''
Descripción del problema: Implementa un método contar_elementos en la clase CalculadoraRecursiva
que reciba una lista y devuelva la cantidad de elementos que contiene de manera recursiva.
'''
def contar_elementos(n):

    if n==[]:
        return 0
    else:
        return 1+len(n[1:])      
 

#contar_elementos()
#calcular_mcd(656,848)
#suma_digitos(124)
#generar_fibonacci(0)
#print(potencia_recursiva(5,3))
generar_fibonacci(8)
#print(serpList[0])
a=[2,"bolillo","cuernito","roll","dona"]
#print(contar_elementos(a))





