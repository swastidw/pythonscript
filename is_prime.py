def is_prime(num):
    is_prime=False
    for i in range(2,num):
        if (num % i)==0:
            print("number is not prime")
            break
        else:
            print("number is prime")
            return(True)
            break
        
def prime_list(a_list):
    l=[]
    for i in range (0,len(a_list)):
        if is_prime(a_list[i])==True:
            l.append(a_list[i])

    print(l)


prime_list([2,3,4,5,6,7,8,9,10,11,12])
