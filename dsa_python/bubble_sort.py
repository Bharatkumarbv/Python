def bubble(A):
    n = len(A)

    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]


if __name__ == '__main__':
    A = list(map(int,input("enter the list of values = ").split()))
    print("original list",A)
    bubble(A)
    print("sorted List",A)
