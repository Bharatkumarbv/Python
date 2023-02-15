#given range of factorial

number = int(input("enter the range of factorial numbers = "))
print("upto given range factorials")
for i in range(10,number+1):
    k = 1
    for j in range(1,i+1):
        k = k*j
    print(str(i),"factorial is = ",k)
