def selection(A):
    n = len(A)

    for i in range(n):
        pos = i

        for j in range(i+1, n):
            if A[j] < A[pos]:
                pos = j

        A[i], A[pos] = A[pos], A[i]


if __name__ == "__main__":
  
    A = list(map(int,input("enter the list of numbers = ").split()))
    selection(A)
    print("sorted list = ",A)
    
