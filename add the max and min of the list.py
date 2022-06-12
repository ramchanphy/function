def fun(k,l,n):
    l.sort()
    if k>=1 and k<=n:
        if n>0:
            if l[k-1]!=l[-k]:
                sum=l[k-1]+l[-k]
                return(sum)
            else:
                return(l[k-1]),l[-k]
print(fun(2,[8,6,7,5,3,2,1],2))