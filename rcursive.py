#sum of the values upto given numbers


def rec(a,n):
    if a<=n: 
        b = a+rec(a+1,n)
        
    else:
        b = 0
    return b

a= int(input("eneter starting number = "))
n = int(input("eneter starting number = "))

print(rec(a,n))







