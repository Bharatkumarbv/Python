def ha(word,new):
    ds = {}
    for i in new:
        ds[i] = word.count(i)
    return ds
    
word = input("enter a string = ")
new= []

for i in word:
    if i not in new:
        new.append(i)

n = ha(word,new)
print(n)
