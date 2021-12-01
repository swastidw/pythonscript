a=[3,30,34,5,9]
list=0
for i in range(0,len(a)):
    while a[i]/10>0:
        l=a[i]/10
    list.append(l)
list.sort
print(list)