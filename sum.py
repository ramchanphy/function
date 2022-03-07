def add_number(num1,num2):
    sum=num1+num2
    print(sum)
add_number(56,12)
def add_number_list(list1,list2):
    i=0
    sum=0
    while i<len(list1):
        sum=list1[i]+list2[i]
        print(sum)
        i+=1
add_number_list([50, 60, 10],[10, 20, 13])