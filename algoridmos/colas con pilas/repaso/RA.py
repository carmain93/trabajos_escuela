class cola:
    def __init__(self):
        self.elementos=[]
    def vacio(self):
        if len(self.elementos)==0:
            return False
        else:
            return True
        
    def agregar(self,nodo):
        self.elementos.append(nodo)
        
    def consultar(self):
        print(self.elementos)
        
    def eliminar(self):
        self.elementos.pop(0)
        
    def acciones(self):
        for i in self.elementos:
            print(i)
            
    def varios(self,datos):
        for i in datos:
            self.agregar(i)
    def limpiar(self):
        self.elementos=[]
        
            
raf= cola()
while len(raf.elementos)>0:
    print("que desea hacer")
    print("1.-agregar")
    print("2.-eliminar")
    print("3.-ver elementos")
    print("4.-agregar varios de golpe")
    print("5.-limpiar y salir")
    i=input("escribe el nuemro de tu opcion: ")
    if(i=="1"):
        raf.agregar(b)
    if(i=="2"):
        raf.eliminar()
    if(i=="3"):
        raf.consultar()
    if(i=="4"):
        raf.agregar()
    if(i=="5"):
        raf.limpiar()
        break
    
class pila:
    def __init__(self):
        self.elementos=[]
    
    def agregar(self,dato):
        self.elementos.append(dato)
    
    def eliminar(self):
        self.elementos.pop(-1)
        
    def limpiar(self):
        self.elementos=[]
    
    def sima(self):
        print(self.elementos[-1])
    
    def tamaño(self):
        print(len(self.elementos))
    
    def mostrar(self):
        print(self.elementos)
    def historial(self):
        for i in self.elementos:
            print(i)
            

rap=pila()

rap.agregar("me levanto")
rap.agregar("voy a la escuela")
rap.agregar("vulevo como")
rap.agregar("me duermo")

#rap.eliminar()
#rap.limpiar()

rap.tamaño()
rap.mostrar()
rap.historial
    
    