x=1
print(x)
print(type(x))
lista= [1,2,3]
lista.append(3)
print(lista)
print(lista.count(3)) #numero de veces que se repite el numero en la lista
print(lista.index(1)) #busca por
print(lista.remove(3))#indicar el dato a borrar
#print(lista.remove[1])#indica que boraras el dato en la posision 0
con1=([2,3,3,4])
con2=([5,3,4,1])
con3=([3,2,5,7])
print(con1+con2+con3)

diccionarios={"uno","dos","tres"}
#print(diccion.keys())
#print(diccionarios.values())
#print(diccionarios.items())
print("\n \nproblemas repaso ****************")
#agera 10 personajes de anime en una lista elimina 3 agrega 5 y mostrando los 
# pesonajes que ocupen los puestos 1 5 7 10 2
di=["lufy","ichigo","ligd","alucard","makoto","zoro","yuta","lala","simon","eren"]
print(di)
di.pop(0)
di.pop(1)
di.pop(3)
di.append("itadori")
di.append("midorilla")
di.append("kririto")
di.append("trevor")
di.append("dante")
print(di[1],di[5],di[7],di[10],di[2])

#crea una tupla con las 10 canciones mas escuchadas en el orden 
# que las has escuchado y ordenandolas por artistas ejecuta le metodo count y el metodo index
print("segundo problema")
t=("")
#crea 3 conjuntos con los datos de tu serie favorita agregando de valores los nombres de los capitulos
#separados por temporada elimina los capitulos que no te gustaran y utilisa el metodo is subsed asi 
#como el metodo interceccion
print("conjuntos")
c={1,2,3,4,5}
print(c)
c.remove(3)
print(c)
#crea un diccionario con 10 videojuegos y sus casa productoras dandoles el valor y key correspondientes
#segun sean el acomodo elimina 3 datos y ejecuta metodos values e items 
# para optener los datos correspondientes
print("diccionario")
d={1:1,3:2,2:1}
print(d.values())
print(d.items())
