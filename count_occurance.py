#Count Occurrences of Element in List

def func(word):
    empty = []
    for i in word:
        if i != " ":
            if i not in empty:
                k = word.count(i)
                empty.append(i)
                print(i,k,end=",")

word = input("enter the word = ")
count = 0
for i in range(len(word)):
    if word[i].isalpha() or word[i] == " ":
        count += 1
if count == len(word):
    
    func(word)
else:
    print("your enter wrong please enter only alphabets")
        
    
