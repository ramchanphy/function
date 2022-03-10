def very_even(n):
    if n==1:
        return 1
    return n+very_even(n-1)
result=very_even(12)
print(result)