def max_subarray(n,array):
    sum=0
    array.sort()
    
    if array[n-1]<0:
        print (array[n-1])
    else:
        temp=array.index(min([i for i in array if i>=0]))
        for i in range(temp,n):
            sum=sum+array[i]
        print(sum)


max_subarray(4,[-1,-2,-3,-4])