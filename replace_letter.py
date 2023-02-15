#Replace All Occurrences of ‘a’ with $ in a String

def rpl(word,i,j):
    k = word.replace(i,j)
    return k

word = input("enter the string = ")
i = input("enter which letter you change = ")
j = input("enter replacing letter = ")

print(rpl(word,i,j))
