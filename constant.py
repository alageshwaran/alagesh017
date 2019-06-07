n=input()
n=ord(n)
if ((n>=65&n<=90)or(n>=97&n<=122)):
    if n==65 or n==69 or n==73 or n==79 or n==85 or n==97 or n==101 or n==105 or n==111 or n==117:
        print('Vowel')
    else:print('Consonant') 
else:print('Invalid')
