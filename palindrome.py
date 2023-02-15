#Palindrome or not

#string = input("enter the string = ")

def stt(string):
    if string == string[::-1]:
        return "It is Palindrome"
    else:
        return "Not a Palindrome"
