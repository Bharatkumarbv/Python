#Palindrome in the given list

def palin(string):
    tr = []
    

    for i in range(len(string)):
        if string[i] == string[i][::-1]:
            tr.append(string[i])

    if len(tr)>0:
        return tr
    else:
        return "No palindromes"
    


string = list(input("enter the  more string = ").split())
k = palin(string)
print(k)
