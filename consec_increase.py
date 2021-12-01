def consec_inc (array):
    for i in range (0,len(array)-2):
        for j in range (i+1,len (array)-1):
            for k in range(j+1,len(array)):

             if array[i]<array[j]<array[k]:
                print("true")
                print(array[i],array[j],array[k])
            else:
                print('false')



consec_inc([2,1,5,2,6,8])