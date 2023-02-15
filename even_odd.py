#print even numbers and odd numbers separeatly

#number = int(input("enter a number = ")
def ev_od(number):
    even = []
    odd = []
    for i in range(number):
        if i %2==0:
            even.append(i)
        else:
            odd.append(i)

    return even,odd
    
#number = int(input("enter a number = "))
#k = ev_od(number)
#print(k)
