#Remove Odd Indexed Characters in a string

def string(word):
    result= ""
    for i in range(1,len(word),2):
        result += word[i]
    return result

word = input("enter a long string = ")
print(string(word))

