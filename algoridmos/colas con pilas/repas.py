from collections import deque
cola=[]
cola=deque()
#Agregar elementos a una cola de una acción secuencial.
cola.append("despertar")
cola.append("ir a la escuela")
cola.append("volver a casa a comer")
cola.append("dormir")
#• Mostrar la cola de una impresión de acciones.
for i in cola:
    print(i)
#• Ciclo que se repita cuando la estructura “Cola” sea >0.
#while len(cola)>0:

print("seigueintes\n\n")
#• Verifica si la estructura está vacía.
if len(cola)<0:
    print("esta vacia")
else:
    print("tiene cosas")
    
#• Agrega un elemento.
def agregar(elemento):
    cola.append(elemento)
#• Consultar elementos.
print(cola)
#• Eliminar elementos.
cola.popleft()
print(cola)
#• Crea un menú en donde se ejecuten las opciones agregar, consultar y eliminar
#cola=[]
print(cola)
print(cola[0])
print(len(cola))
