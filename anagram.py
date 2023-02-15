#anagram

def string(word1, word2):
    count = 0
    for i in word2:
        if word2.count(i) == word1.count(i):
            count += 1
    if count == len(word2):
        return "It is an anagram"
    else:
        return "It is not an anagram"

#word1 = input("enter a string ")
#word2 = input("enter a second string ")

#string(word1,word2)
