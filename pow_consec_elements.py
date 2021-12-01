def pow_consec_elements (name):
    count=1
    for i in range (0,len(name)-1):
        if name[i]==name[i+1]:
            count+=1
            print(name[i],count)
    count=1



pow_consec_elements("swaaastiiiiii")