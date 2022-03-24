def function(A):
    i=0
    x=[]
    while i<len(A):
        if A[i] != A[i-1]:
            x.append(A[i])
        i += 1
    print(x)
function(A=input("enter the character"))