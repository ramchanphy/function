def calculater(number_x,number_y,operation):
    if operation=="add":
        sum=number_x+number_y
        print(sum)
    elif operation=="sub":
        sub=number_x-number_y
        print(sub)
    elif operation=="multiply":
        mul=number_x*number_y
        print(mul)
    else:
        div=number_x%number_y
        print(div)
calculater(20,25,"add")
calculater(40,3,"sub")
calculater(10,4,"multiply")
calculater(40,4,"div")    