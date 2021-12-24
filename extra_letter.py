def extra_letter (a,b):
   alphabet=(a and b)
   alphabetdict=dict()
   for char in alphabet:
       alphabetdict[char]=0
   for i in a:
      if i not in alphabetdict:
        print (i)
       
extra_letter ("flower","flowe")


