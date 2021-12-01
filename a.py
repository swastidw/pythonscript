def product_maxmin (array):
    i=0
    max=0
    min=array[0]
    for i in range (0,len(array)):
        if array[i]>=max:
            max=array[i]
        if array[i]<=array[0]:
            min=array[i]
    product=max*min
    print (product)
product_maxmin([1000,23,344,2344,22343,500,3])