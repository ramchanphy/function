def fun(n):
    i=0
    b=[]
    sum=0
    while i<len(n):
        sum+=n[i]
        b.append(n[i])
        i+=1
    b.append(sum)
    return(b)
print(fun([1,2,3]))