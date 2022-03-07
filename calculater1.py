operation=input("enter the sign")
def add(num_x,num_y):
    sum=num_x+num_y
    print(sum)
def sub(num_x,num_y):
    sub=num_x-num_y
    print(sub)
def multiply(num_x,num_y):
    multiply=num_x*num_y
    print(multiply)
def div(num_x,num_y):
    div=num_x/num_y
    print(div)
def main():
    if operation=="add":
        add(4,5)
    elif operation=="sub":
        sub(9,3)
    elif operation=="multiply":
        multiply(2,3)
    elif operation=="div":
        div(4,2)
main()