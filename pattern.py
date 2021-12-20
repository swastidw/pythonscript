def pattern(num):
    len=1
    for i in range (0,num):
        print (num*" "+len*"*")
        len+=1
        num=num-1
pattern(5)