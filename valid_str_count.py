def valid_str(l):
    invalid=0
    for i in l:
        flag=0
        for j in i:
            if j.isalpha() or j==" ":
                pass
            else:
                flag=1
        if flag==1:
            print("hi",i)
            invalid+=1
    valid=len(l)-invalid
    print(valid)
    print(invalid)
l=[]
n=int(input())
for i in range(n):
    a=input()
    l.append(a)
valid_str(l)
