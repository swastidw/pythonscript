def array_rotate (array,k):
    temp1=0
    temp2=array[len(array)-1]
    for i in range(0,k):
        for j in range (0,len(array)):
            temp1=array[j]
            array[j]=temp2
            temp2=temp1
            
            




            

    print (array)



array_rotate([5,7,8,4,6],1)
