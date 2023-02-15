# Upto given range prime numbers

def arm(number):
    result = []
    for j in range(1,number+1):
        k = 0
        for i in str(j):
            k = k +pow(int(i),len(str(j)))

        if k == j:
            result.append(j)
    return result
    

number = int(input("enter the number = "))
print(arm(number))
        
