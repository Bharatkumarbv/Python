#Tuple swapping

def tep(tuple1,tuple2):
    tuple1,tuple2 = tuple2,tuple1
    return tuple1,tuple2

tuple1 = tuple(map(int,input("enter a numbers = ").split()))
tuple2 = tuple(map(int,input("enter a numbers = ").split()))
print(tep(tuple1,tuple2))


 
