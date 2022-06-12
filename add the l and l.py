k = int(input("enter"))
n = int(input("enter1"))
l = []

for i in range(0, n):
    p = int(input())
    l.append(p)
    
def SumOfNumbers(l,n,k):
    l.sort()
    if k>=1 and k<=n:
        if n>0:
            if l[k-1]!=l[-k]:
                sum=l[k-1]+l[-k]
                return sum
            else:
                return(l[k-1],l[-k])

result = SumOfNumbers(l,n,k)
print(result)

