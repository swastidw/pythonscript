def com_string (a):
    j=0
    for i in range (0,len(a)-1):
        if a[i][j]==a[i+1][j]:

            j=j+1
            print (a[0][:j+1])
        else:
            print ("")


com_string(["flower","flour","florist"])


