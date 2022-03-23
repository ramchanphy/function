# def unique_order(n):
#     i=0
#     b=[]
#     k=1
#     while i<len(n): 
#         if n[i]!=n[k]:
#             b.append(n[i])
#         i+=1
#         k+=1
#     print(b)
# unique_order(["aaaabbbccccddhaaa"])

a="aaannnrryyyuuuvv"
i=0
k=1
c=[]
while i<len(a):
    if a[i]!=a[k]:
        print(a[i])
    else:
        print("none")
    i+=1
    k+=1
