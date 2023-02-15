#prime numbers printing



def lists(number):
    result = []
    if number <=1:
        return "Not a prime number"
    else:
        
        for i in range(2,number+1):
            count = 0
            for j in range(2,i+1):
                if i%j==0:
                    count += 1
            if count == 1:
                result.append(i)
        return result


number = int(input("enter thge range of numbers = "))
print(lists(number))
