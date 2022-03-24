def fun(num):
    a=num*num
    return(a)
def fun2(num):
    b=num*num*num
    return(b)
def main():
    c=fun(num)+fun2(num)
    return(c)
num=int(input("enter the number"))
print(main())
        