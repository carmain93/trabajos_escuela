from collections import deque
#definir pila
historial_acciones=deque()
#agregar acciones
historial_acciones.append('abrir documento')
historial_acciones.append('escribir parrafo')
historial_acciones.append('editar estilo')
historial_acciones.append('guardar documento')

#imprimir historial
print(f'historial de acciones {historial_acciones}')
print('#############################3')

#cilco
while len(historial_acciones)>0:
    ultima_accion=historial_acciones.pop()
    print(f'acciones mas reciente {ultima_accion}')
    print(f'origen: {historial_acciones}')
    print('#####################################')