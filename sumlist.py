def function_sum(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i+=1
    print(sum)
function_sum([1, 2, 3, 4, 5])