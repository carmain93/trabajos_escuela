class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            # El valor ya existe en el árbol
            pass

    def imprimir_inorden(self, nodo_actual):
        if nodo_actual:
            self.imprimir_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self.imprimir_inorden(nodo_actual.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual
        
        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            
            temp = self._encontrar_minimo(nodo_actual.derecha)
            nodo_actual.valor = temp.valor
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, temp.valor)
        
        return nodo_actual

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
    
    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecha)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Árbol antes de eliminar 5:")
arbol.imprimir_inorden(arbol.raiz)

arbol.eliminar(5)
print("el valor de ",arbol.buscar(3))
print("Árbol después de eliminar 5:")
arbol.imprimir_inorden(arbol.raiz)
