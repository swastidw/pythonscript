def pow (x,n):
    pow=1
    if n>0:

       for i in range (0,n):
          pow=x*pow
    elif n==0:
        pow=1
    else:
        for i in range (0,abs(n)):
           pow=(1/x)*pow
    print (pow)
pow(2,0)