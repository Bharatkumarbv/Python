def search(A, key):
    n = len(A)

    for index, val in enumerate(A):
        if val == key:
            return index

    return -1


if __name__ == "__main__":
    A = list(map(int,input("enter the list of values = ").split()))
    key =int(input("searching value = ")) 
    res = search(A, key)
    print("the index value is = ",res)
