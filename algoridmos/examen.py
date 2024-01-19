class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None
        
        #definicion del tipo de nodo

class ListaEnlazada:
        def __init__(self):
            self.cabeza = None
                #metodo agregar elemento

        def agregar_elemento(self, valor):
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza=nuevo_nodo
            #metodo impresion de lsita
            
        def imprimir_lista(self):
            actual = self.cabeza
            while actual:
                print(actual.valor, end=" -> ")
                actual=actual.siguiente
            print("None")

#crear lista
mi_lista=ListaEnlazada()
mi_lista.agregar_elemento(3)
mi_lista.agregar_elemento(4)
mi_lista.imprimir_lista()