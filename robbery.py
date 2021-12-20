def robbery (money):
    robsum_even=sum(money[::2])
    robsum_odd=sum(money[1::2])
    if robsum_even>=robsum_odd:
        print (robsum_even)
    else:
        print(robsum_odd)
robbery([1,2,3,1,])
    

        