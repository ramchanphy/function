def function():
    i=0
    f=0
    s=1
    while i<=10:
        if i<=1:
            t=i
        else:
            t=f+s
            f=s
            s=t
        i+=1
        print(t,end=",")
function()        