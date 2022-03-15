print("welcome to SBI world")
print("please insert your card\nDo not remove until the transaction is completed" )
balance=50000
pin=1234
def function():
    user=input("englist or hindi: ")
    if user=="eng":
        print("choose your transaction\n1.balance_enquiry\n2.cash withdrawl\n3.deposit\n4.pin_generation\n5.quit")
function()
transaction=int(input("select your option:- "))
def balance_enquiry():
    print("balance_enquiry")
    print("for current press 1\nfor saving press 2")
    balance_enquiry=int(input("enter the pin number"))
    if balance_enquiry==1:
        print("enter your pin")
        user=int(input("enter the number"))
        if user==pin:
            print("your account balance=",balance)
    else:
        print(balance)
def withdrawl():
    print("cash withdrawl")
    user=int(input("enter the pin:-"))
    if pin==user:
        amount=int(input("enter the amount"))
        remainder=balance-amount
        print("remaining balance =",remainder)
def deposit():
    print("deposit")
    amount=int(input("enter the amount"))
    current_balance=balance+amount
    print(current_balance)
def pin_generation():
    print("pin_generation")
    if pin==pin:
        new_pin=int(input("enter the new_pin number"))
        pin=new_pin
        print("new_pin",pin)
def quit():
    print("quit\nthank you for visiting the SBI bank")
def main():
    if transaction==1:
        balance_enquiry()
    if transaction==2:
        withdrawl()
    if transaction==3:
        deposit()
    if transaction==4:
        pin_generation()
    if transaction==5:
        quit()
main()
        
            
                         
    