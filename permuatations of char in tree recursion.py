#permuatations of char in tree recursion

def permute(s,bucket=' '):
    if not s:
        print(bucket)
        return
    for i in range(len(s)):
        ns=s[:i]+s[i+1:]
        permute(ns,bucket+s[i])
text=input("enter a name/word:")
print("possibilities of combinations......")
permute(text)

O/P:-
enter a name/word:abcd
possibilities of combinations......
abcd
 abdc
 acbd
 acdb
 adbc
 adcb
 bacd
 badc
 bcad
 bcda
 bdac
 bdca
 cabd
 cadb
 cbad
 cbda
 cdab
 cdba
 dabc
 dacb
 dbac
 dbca
 dcab
 dcba
