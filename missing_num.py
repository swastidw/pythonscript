def missing_num (n,arr):
    arr.sort()
    var=min([i for i in arr if i>=0])
    
    temp=arr.index(min([i for i in arr if i>=0]))
    
    for i in range (temp,n-1):
        if arr[i+1]==var+1:
            var=var+1
    print(var+1)



missing_num (5,[0,-10,3,1,-20])