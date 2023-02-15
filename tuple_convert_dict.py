#Write a Python program to convert a tuple to a dictionary

def convert(t1,t2,t3,t4):
    t =(t1,t2,t3,t4)
    k = {}
    for i in range(len(t)):
        k[t[i][0]] = t[i][1]
        
    return k

t1 = tuple(input("enter the 2 values ").split())
t2 = tuple(input("enter the 2 values ").split())
t3 = tuple(input("enter the 2 values ").split())
t4 = tuple(input("enter the 2 values ").split())
print(convert(t1,t2,t3,t4))


