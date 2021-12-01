def max_product(array):
    for i in range(0,len(array)):
        for j in range (i+1,len(array)):
            if array[j]>=array[i]:
                maxim=array[i]
                array[i]=array[j]
                array[j]=maxim

    product=array[0]*array[1] 
    print(product)           
    
    
     
        


    
    
    

max_product([1000,23,344,234,223,500,3])