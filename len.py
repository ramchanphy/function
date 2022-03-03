def function_name(name):
    i=0
    count=0
    while i<len(name):
        j=0
        while j<len(name[i]):
            count+=1
            j+=1
        i+=1
        print(count)
function_name("hello","welcome")
function_name("sonu","nonu")
            