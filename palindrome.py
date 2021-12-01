def palindrome(string):
    for i in range (0,len(string)):
        length =len(string)-i-1
        if string[i]!=string[length]:
            print ("not a palindrome")
        else:
            print("a palindrome")

          



palindrome("queen")

