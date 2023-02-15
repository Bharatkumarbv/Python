#Remove duplicates

def dup(lst):
    empty = []
    duplicates = []
    for i in range(len(lst)):
        if lst[i] not in empty:
            empty.append(lst[i])
        else:
            duplicates.append(lst[i])
            
    print("original list = ",lst)
    print("without duplicates = ",empty)
    print("duplicate numbers are = ",duplicates)
    return empty

lst = list(map(int,input("enter the list of numbers = ").split()))
dup(lst)
