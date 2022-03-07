def string(sen):
    i=0
    count=0
    count1=0
    while i<len(sen):
        if sen[i].isupper():
            count+=1
        elif sen[i].islower():
            count1+=1
        i+=1
    print(count,count1)
string("The quick Brow Fox")
        
    