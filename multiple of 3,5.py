def function_num(num):
    i=1
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            sum+=i
        i+=1
    print(sum)
function_num(10)

    