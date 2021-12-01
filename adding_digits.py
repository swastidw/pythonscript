def digit(num):
    i=0
    sum=0
    for i in range(0,10):
        
        rem=num%10
        sum=rem+sum
        num=num/10
    print (sum)



digit(9180)

