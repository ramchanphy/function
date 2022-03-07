def function():
    user=int(input("enter the number"))
    temp=user
    sum=0
    rem=0
    while user>0:
        rem=user%10
        sum=sum+rem
        user=user//10
    print(sum)
    if temp%sum==0:
        print("harshad")
    else:
        print("not harshad")
function()