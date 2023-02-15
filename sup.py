#search the word in list

def search(array,word):
    result = []
    for i in range(0,len(array)):
        if array[i].startswith(word):
            result.append(array[i])
    return result


array = list(input("enter a list of words ").split())
a = input("enter the search  word")
print(search(array,a))
