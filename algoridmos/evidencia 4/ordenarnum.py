l=[2,1,3,5,6,4,7]
print(f"lista ordenada: {l}")

for i in range(len(l)):
    for j in range(i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            
print(f"lista ordenada: {l}")