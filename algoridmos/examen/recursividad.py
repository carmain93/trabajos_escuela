#Crea una función para generar la secuencia de Fibonacci hasta el décimo término.

def fibonacci(n):
    
    if n==1:
        val=1
    elif n == 2:
        val=1
    elif n > 2:
        val = fibonacci(n-1) + fibonacci(n-2)
        if val > 55:
           print("no es posible devolver un valor superior al decimo de la secuencia")
           return 55
       
    return val


print(fibonacci(4))