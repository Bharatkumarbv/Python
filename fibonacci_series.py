#fibonacci series

#number = int(input("enter a number:"))
def fib(num):
    a = 1
    b = 1
    k = ""
    for i in range(num):
        print(a,end=" ")
        k = k+str(a)
        c = a+b
        a = b
        b = c
    
    print(k)

    
    
