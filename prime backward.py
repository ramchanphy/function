def function(n):
    i=1
    num=[]
    while i<=n:
        count=0
        j=2
        while j<=i//2:
            if i%j==0:
                count = count + 1
            j+=1
        if count==0 and i!=1:
            if i>11:
                x=i%10
                y=i//10
                z=str(x)+str(y)
                num.append(int(z))
        i+=1
    return(num)
def fun(num):
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
n=int(input("enter the number:-"))
print(function(n))
fun(function(n))
