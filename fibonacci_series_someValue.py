#fibonacci series nth number

def fibb(number):
    a = 0
    b = 1

    for i in range(1,number):
        a,b=b,a+b
    
    return a

'''number = int(input("enter a number:"))
k = fibb(number)
print(k)'''

    
    
