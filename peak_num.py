def peak_num(nums):
    l=[]
    for i in range (1,len(nums)-1):
        if nums[i-1]<nums[i]>nums[i+1]:
            l.append(nums[i])
    print(l)


peak_num([1,2,1,3,5,6,4])