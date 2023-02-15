# tuple convert into list

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
k = list(tuple1)
del k[2]
k.remove("apple")
print(tuple(k))
