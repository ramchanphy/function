# def function(A):
#     i=0
#     x=""
#     while i<len(A):
#         if A[i] != A[i-1]:
#             x+=A[i]
#         i += 1
#     print(x)
# function(["e","n","t","e","e","t","t","n"])

l="pwwkew"
a=""
e=""
f=""
c1=0
c2=0
c3=0
i=0
while i<len(l):
    if  l[i]!=l[i-1] and l[i] not in a:
        a+=l[i]
        c1+=1
    elif l[i]!=l[i-1] and l[i] not in e :
        e+=l[i]
        c2+=1
    else:
        f+=l[i]
        c3+=1
        
    i+=1
if len(a)>len(e) and len(a)>len(f):
    print(c1)
    print(a)
elif len(e)>len(a) and len(e)>len(f):
    print(c2)
    print(e)
else:
    print(c3)
    print(f)