def anagrams(w1,w2):
    w1=sorted(w1)
    w2=sorted(w2)
    for i in range(0,len(w1)):
            if len(w1)==len(w2) and w1[i]==w2[i]:
                print("strings are anagrams")
                        
    
    
        
            
            

anagrams("silent","listen")