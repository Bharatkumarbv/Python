#swap first number and last number

def lst(l):
    
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    return l

    

l = list(map(int,input("Enter the list of number = ").split()))
print(lst(l))
