# vowels deleted in string

def string(word):
    
    vowels = "AEIOUaeiou"
    res = ""
    for i in word:
        if i not in vowels:
            res += i
    print("without vowels in given word = ",res)

word = input("enter a string = ")
string(word)
