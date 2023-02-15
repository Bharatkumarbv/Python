# string slicing

def string(word,n):
    if n<=len(word):
        return word[n:]
    else:
        return "this index value not exist"

word = input("enter a word = ")
n = int(input("start index number given word = "))
print(string(word,n))
