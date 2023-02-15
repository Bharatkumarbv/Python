
def sea(a,b):
    empty = []
    if a != empty:
        a.pop()
        b = b+1
        sea(a,b)
        
         
    else:
        print("len of the list is = ",b)

a = list(map(int,input("enter the list of numbers").split()))
b = 0
sea(a,b)

