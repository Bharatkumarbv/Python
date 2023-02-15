# how many vowels in string


def string(word):
    vowels = "AEIOUaeiou"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

#word = input("enter a string = ")
#print(string(word))
