def function_min(list):
    i=0
    min=list[0]
    while i<len(list):
        if min>=list[i]:
            min=list[i]
        i+=1
    print(min)
function_min([8, 6, 4, 8, 4, 50, 2, 7])
            