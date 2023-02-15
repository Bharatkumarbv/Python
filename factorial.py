#factorial of given number


def fac(number):
    k = 1
    for i in range(1,number+1):
        k = k*i

    return k
