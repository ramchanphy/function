def unorder_list(num):
    i=0
    a=[]
    while i<len(num):
        a.append(num[i])
        i+=1
    a.sort()
    print(a)
unorder_list([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])