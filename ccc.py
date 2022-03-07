def function(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i+=1
    print(a)
function([1,2,3,3,3,3,4,5])