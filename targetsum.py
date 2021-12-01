def targetsum(number,sum):
 n=0
 k=0
 for k in number:
   n+=1  
 print(n)
 for i in range(0,n):
    for j in range(0,n):
        if number[i]+number[j]==sum:
            break
 print(number[i],number[j])



targetsum([3,4,5,6,7,7,8,9,3,4,5],9)