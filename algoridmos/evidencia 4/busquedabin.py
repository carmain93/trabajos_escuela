def bus(arr, elemento):
    inicio = 0
    fin = len(arr) - 1

    while inicio <= fin:
        m = (inicio + fin) // 2

        if arr[m] == elemento:
            return m
        
        elif arr[m] < elemento:
            inicio = m + 1
        
        else:
            fin = m - 1

    return -1


l=[1, 2, 3, 4, 5, 6, 7]
print(f"arreglo: {l}")
n=5
print(f"numero a buscar: {n}")
res = bus(l,n)
if res != -1:
    print(f"El elemento {n} está en la posición {res}.")
else:
    print(f"El elemento {n} no está en el arreglo.")


