'''Write a Python code to find numbers and alphabets from the given string and put it in
one list. The list will have two elements – the first element is a type of string that contains the alphabet and the second element is a type of integer. The input string will not have any special characters. The input string can have either the combination of Alphabets and Numbers or only Alphabets or only Numbers or it can be an empty string. Define a function to build a logic that returns a list. This list will contain a string first followed by numbers (must be in an integer format).'''
def str_num(s):
    a=""
    n=""
    l=[]
    for i in s:
        if i.isalpha():
            a=a+i
        else:
            n=n+i
    if n:
        n=int(n)
    for j in a,n:
        if j:
            l.append(j)
    return l
s=input()
print(str_num(s))
