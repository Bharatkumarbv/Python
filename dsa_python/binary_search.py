def search(A, key):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == key:
            return mid
        
        elif A[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    A = list(map(int,input("enter the list of values = ").split()))
    key = int(input("searching value = "))
    res = search(A, key)
    print(res)
