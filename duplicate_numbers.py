def duplicate(a_list):
    l=[]
    length=(len(a_list))
    for i in range (0,length):
        if a_list[i]==a_list[i-1]:
            l.append(a_list[i])
    print(l)


duplicate([0,0,1,1,1,2,2,3,4])