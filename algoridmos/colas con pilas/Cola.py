from collections import deque
impresion = deque()

#agregar elemtos
impresion.append('primer documento')
impresion.append('segundo documento')
impresion.append('tercero documento')
impresion.append('cuarta documento')

# mostrar cola de impresion
print(f'cola de impresion {impresion}')
print('-------------------------------')

# ciclo que funciona mientras alla archivos en la estructura

while len(impresion)>0:
    siguiente_elemento= impresion.popleft()
    print(f'siguiente elemento: {siguiente_elemento}')
    print(f'cola de impresion {impresion}')
    print('######################')