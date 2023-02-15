


def tup(a,b):
    b = a
    return b[0],b[1] 

    
a = tuple(map(int,input("enter the numbers").split()))
b = tuple(input("enter the words").split())

print(tup(a,b))




