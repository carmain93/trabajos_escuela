'''Crea tres conjuntos:
Conjunto 1: Los primeros 10 números impares.
Conjunto 2: Los primeros 10 números pares.
Conjunto 3: Los primeros 10 números naturales.'''
c1={1,3,5,7,9,11,13,15,17,19}
c2={2,4,6,8,10,12,14,16,18,20}
c3={1,2,3,4,5,6,7,8,9,10}
#Imprime los conjuntos 1, 2 y 3 antes de realizar cualquier operación.
print("conjunto1= ",c1,"\nconjunto2= ",c2,"\nconcunto3= ",c3)
#Ejecuta las operaciones para saber qué datos se incluyen en los conjuntos 1 y 3, y 2 y 3. Para esto, puedes usar la operación de intersección.
a=c1.intersection(c3)
b=c2.intersection(c3)
print()
#Imprime los conjuntos 1, 2 y 3 después de la operación, así como los resultados de las intersecciones
print("conjunto1= ",c1,"\nconjunto2= ",c2,"\nconcunto3= ",c3,"\ninterccecion1= ",a,"\ninterceccion2= ",b)