#Crea una lista con los primeros 15 números naturales (empezando desde 0).
li=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(li)
#Modifica las posiciones 5, 7, 9 y 11 de la lista con su respectivo nombre en formato de cadena de texto.
li[5]="cinco"
li[7]="siete"
li[9]="nueve"
li[11]="once"
print(li)
#Elimina los elementos en las posiciones 2, 4 y 6 de la lista.
li.pop(2)
li.pop(4)
li.pop(6)
print(li)
#Agrega los números correspondientes a la secuencia del último dígito al final de la lista.
li.append(2)
li.append(4)
li.append(6)
print(li)
#Imprime la lista inicial,  +
# la lista después de las modificaciones, +
# la lista después de las eliminaciones  +
# la lista final después de todos los cambios. +
