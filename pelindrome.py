def function():
    num=int(input("enter the number"))
    temp=num
    rev=0
    while num>0:
        d=num%10
        rev=rev*10+d
        num=num//10
    print(rev)
    if temp==rev:
        print("palindrome")
    else:
        print("not palindrome")
function()