def max_min (array):
    max=0
    for i in range (0,len(array)):
        if array[i]>=max:
            max=array[i]
    print (max)    
max_min([2,6,7,9,11])    