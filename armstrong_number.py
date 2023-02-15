#Armstrong number

def arm(number):
    l = str(number)
    k = 0
    for i in l:
        k = k +pow(int(i),len(l))

    if k == number:
        return True
    else:
        return False

#number = input("enter the number = ")
#arm(number)
        
