# Merge two lists and sort it

def lst(l1,l2):
    l1.extend(l2)
    l1.sort()
    return l1

l1 = list(map(int,input("enter a l1 list of numbers = ").split()))
l2 = list(map(int,input("enter a l2 list of numbers = ").split()))
print(lst(l1,l2))


