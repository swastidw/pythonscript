def min_sum(num):
    list=[]
    length=0
    a=0
    b=0
    
    length=len(str(num))
    for i in range(0,length):
        dig=num%10
        list.append(dig)
        num=int(num/10)
    list.sort()
    print(list)
    for i in range(0,length):
        if i%2==0:

            a=a*10+list[i]
        else:
            b=b*10+list[i]
    sum=a+b
    print(sum)
min_sum(4325)