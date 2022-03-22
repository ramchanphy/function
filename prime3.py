def fun():
    num=[]
    a=[]
    k=0
    while k<len(num):
        z=2
        count=0
        while z<=num[k]//2:
            if num[k]%z==0:
                count+=1
            z+=1
        if count==0 and num[k]!=1:
            a.append(num[k])
        k+=1
    print(a)
fun()