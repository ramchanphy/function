
# def create():
#     length=int(input("enter the length:-"))
#     i=0
#     list1=[]
#     while i<length:
#         n=input("enter the elements:- ")
#         list1.append(n)
#         i+=1
#     return list1
# def second(list1):
#     i=0
#     while i<len(list1):
#         if list1[i].isdigit():
#             print("yes")
#             break
#         i+=1
# print(create())
# second("list1")

def create(length):
    # length=int(input("enter the length:-"))
    i=1
    list1=[]
    while i<=length:
        n=input("enter the elements:- ")
        list1.append(n)
        i+=1
    return list1
def second(list1):
    j=0
    while j<len(list1):
        if list1[j].isdigit():
            print("yes")
            break
        j+=1
length=int(input("enter the number:-"))
print(create(length))
second(create(length))