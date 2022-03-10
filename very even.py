#Write a function that returns True if the number is a very even number.
# If a number is a single digit then it is simply "very even" 
# if it is even. If it has 2 or more digits, it is "very even" 
# if the sum of its digit is " very even"

def function(n):
    x=str(n)
    i=0
    sum=0
    while i<len(x):
        sum=sum+int(x[i])
        i+=1
    if sum>=1 and sum<=9:
        # return(sum)
        if sum%2==0:
            print("very even")
    else:
        y=str(sum)
        j=0
        sum2=0
        while j<len(y):
            sum2=sum2+int(y[j])
            j+=1
        if sum2%2==0:
            print(sum2,"very even")
        else:
            print(sum2,"odd")
function(n=int(input("enter the number")))
    
    
        

        