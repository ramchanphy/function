def function_max(maximum):
    i=0
    max=0
    while i<len(maximum):
        if max<=maximum[i]:
            max=maximum[i]
        i+=1
    print(max)
function_max([3, 5, 7, 34, 2, 89, 2, 5])