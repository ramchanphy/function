def fun(n):
    i=0
    j=1
    a=[]
    while j<len(n):
        if n[i]!=n[j]:
            a.append(n[i])
        i+=1
        j+=1
    a.append(n[i])
    print(a)
fun(n=input("enter the number"))