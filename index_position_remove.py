# Remove the nth Index Character from a Non-Empty String

def ind(word, n):
    k = ""
    for i in range(len(word)):
        if i != n-1:
            k += word[i]
    return k
    

word = input("enter a string = ")
n = int(input("enter a number = "))
ind(word,n)
