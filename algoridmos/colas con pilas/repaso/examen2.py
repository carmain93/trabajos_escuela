class pila:
    def __init__(self):
        self.elementos=[]
        
    def agregar(self,nodo):
        self.elementos.append(nodo)
        
    def mostrar(self):
        print(self.elementos)
    def limpiar(self):
        self.elementos=[]
        
    def tamaño(self):
        print(len(self.elementos))
        
    def sima(self):
        print(self.elementos[-1])
        
    def eliminar(self):
        self.elementos.pop(-1)
    

a= pila()
a.agregar("")
a.agregar("adios")
a.agregar("cuidado")
#a.limpiar()
a.mostrar()
a.tamaño()
a.sima()
a.eliminar()
a.mostrar()
a.limpiar()
a.agregar("1.-me levanto y desayuno ")
a.agregar("2.-voy a la escuela ")
a.agregar("3.-vuelvo a mi casa a descansar ")
a.agregar("4.-me duermo")
a.mostrar()
