def expanded_form(num):
    a= []
    i = len(str(num)) -1
    for s in str(num):
        if s != "0":
            a.append(s + "0" * i)
        i -= 1
    return " + ".join(a)
print(expanded_form(int(input("enter the number"))))