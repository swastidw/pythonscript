def arr_jump (array):
    for i in range (0,len(array)-1):
        pointer=array[i]
        i=i+pointer
    if i==len(array)-1:
        print ("true")
    else:
        print ("false")
    
arr_jump([3,2,1,0,4])