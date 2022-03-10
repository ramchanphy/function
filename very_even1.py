def very_even(n):
    x=str(n)
    i=0
    sum=0
    while i<len(x):
        sum=sum+int(x[i])
        i+=1
    s=str(sum)
    if len(s)==1:
        print(s,"very even")
    else:
        n=s
        return(very_even(sum))
num=int(input("enter the number: "))
very_even(num)
                            