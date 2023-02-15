def insertion(A):
    n = len(A)

    for i in range(1, n):
        current = A[i]
        pos = i

        while pos > 0 and A[pos - 1] > current:
            A[pos] = A[pos - 1]
            pos -= 1

        A[pos] = current


if __name__ == '__main__':
    A = list(map(int,input("enter the list of numbers = ").split()))
    print("original list = ",A)
    insertion(A)
    print("sorted list = ",A)
