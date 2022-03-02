def function_list(num):
    i=0
    a=[]
    while i<len(num):
        a.append(num[i])
        i+=1
    return(a)
print(function_list([1,5,10,15,50]))