class Cola:
    def __init__(self):
        self.elementos=[]
#metodo de la verificacion de la cola bacia xd
    def vacio(self):
        return self.elementos==[]
#        if len(self.elementos)==0:
    def insertar(self,nodo):
        self.elementos.append(nodo)
        print("elemento fue añadido")
    def eliminar(self):
        if self.vacio():
            print("la estructura esta vacia")
        else:
            self.elementos.pop(0)
#metodo para consultar
    def consultar(self):
        if self.vacio():
            print('estructura vacia')
        else:
            print(self.elementos)
            
    def sumar(self):
        if self.vacio():
            print("estructura vacia")
        else:
            s=0
            for i in self.elementos:
                s=s+int(i)
            print("la suma de los elemento es: ",s)
            return s
    def resta(self):
        if self.vacio():
            print("lista bacia")
        else:
            resta = int(self.elementos[0])
            for i in self.elementos[1:]:
                resta -=int(i)
            print("la resta de elementos es: ",resta)
    def promedio(self):
        if self.vacio():
            print("estructura vacia")
        else:
            promedio = self.sumar()/len(self.elementos)
            print("El promedio es: ",promedio)
#objeto
obj=Cola()
while True:
    print("1.- Insertar")
    print("2.- Consultar")
    print("3.- Eliminar")
    print("4.- salir")
    print("5.-sumar")
    print("6.-resta")
    print("7.-promedio")
    
    opcion=int(input("escribe el numero de la opcion: "))
    if opcion==1:
        nodo=input("Escribe el nuevo elemento: ")
        obj.insertar(nodo)
    elif opcion ==2:
        obj.consultar()
    elif opcion ==3:
        obj.eliminar()
    elif opcion==4:
        break
    elif opcion==5:
        obj.sumar()
    elif opcion==6:
        obj.resta()
    elif opcion==7:
        obj.promedio()
    else:
        print("opcion no valida")
        