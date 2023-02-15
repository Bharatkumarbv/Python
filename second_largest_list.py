# Find the  2nd largest number

def lst(l1):
    l1.sort()
    return (l1[-2])

l1= list(map(int,input("enter a list of number = ").split()))
print(lst(l1))
