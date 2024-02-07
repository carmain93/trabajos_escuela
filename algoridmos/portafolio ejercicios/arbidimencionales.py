md=[
    [15,12,3],
    [32,54,10],
    [10,20,30]
    ]
print(md[0][1])
md[0][1]=10
print(md[0][1])
suma =0
p=0
for fila in md:
    for num in fila: 
        suma+=num
        p+=1

print(suma)