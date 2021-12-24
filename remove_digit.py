def remove_digit (num,k):
    l=[]
    for i in str(num):
        l.append(i)
    while k>0:
       if i!=min(l):
           l.pop(int(min(l)))
           k=k-1
           print (l)


remove_digit(143219,3)
