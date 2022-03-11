print("welcome to SBI world")
print("please insert your card\nDo not remove until the transaction is completed" )
def function():
    pin=1234
    balance=50000
    user=input("englist or hindi: ")
    if user=="eng":
        print("choose your transaction\n1.balance_enquiry\n2.cash withdrawl\n3.deposit\n4.pin_generation\n5.quit")
        transaction=int(input("enter the number: "))
        if transaction==1:
            print("balance_enquiry")
            print("for current press 1\nfor saving press 2")
            balance_enquiry=int(input("enter the number"))
            if balance_enquiry==1:
                print("enter your pin")
                user=int(input("enter the number"))
                if pin==user:
                    print("your account balance=",balance)
            else:
                print(balance)
        elif transaction==2:
            print("cash withdrawl")
            user=int(input("enter the pin:-"))
            if pin==user:
                amount=int(input("enter the amount"))
                remainder=balance-amount
            print("remaining balance =",remainder)
        elif transaction==3:
            print("deposit")
            amount=int(input("enter the amount"))
            current_balance=balance+amount
            print(current_balance)
        elif transaction==4:
            print("pin_generation")
            if pin==pin:
                new_pin=int(input("enter the number"))
                pin=new_pin
            print("new_pin",pin)
        else:
            print("quit\nthank you for visiting the SBI bank")
            
function()
                         
    