def wave_array (arr,n):
    l=[]
    if n%2==0:
       l=arr[::2]
       arr[::2]=arr[1::2]
       arr[1::2]=l
       print (arr)
    else:
        l=arr[:n-1:2]
        arr[:n-1:2]=arr[1::2]
        arr[1::2]=l
        print(arr)
    

wave_array([1,2,3,4,5],5)