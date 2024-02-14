def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)


arr = [3, 6, 8, 10, 1, 2, 1]
arreglo_ordenado = quicksort(arr)
print("Arreglo ordenado:", arreglo_ordenado)
