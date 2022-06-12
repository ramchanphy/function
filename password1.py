def fun(password):
    d="0123456789"
    ca="A-Z"
    a="a-z"
    c="*_-@!"
    # sum=0
    e=0
    b=0
    f=0
    g=0
    if password[0] not in d:
        i=0
        while i<len(password):
            if password[i] in d:
                e=1
            elif password[i] in ca:
                b=1
            elif password[i] in a:
                f=1
            elif password[i] in c:
                g=1
            i+=1
        if (e+b+f+g)<4:
            print(0)
        else:
            print(1)
    else:
        print(0)
password=input()
fun(password)



