#Find Largest Number in a List

def lst(l1):
    #k = max(l1)
    #print(k)
    max_value = l1[0]
    for i in range(len(l1)-1):
        if max_value < l1[i+1]:
            max_value = l1[i+1]

    return max_value

l1= list(map(int,input("enter the list of numbers = ").split()))
m = lst(l1)
print(m)

