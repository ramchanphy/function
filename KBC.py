question_list=["How many continents are there?","what is the capital of india?","NG mei kaun se cource padhaya jaata hai?"]
options_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","Agriculture"]]
solution_list=[3,4,1] 
def function(index):
    i=0
    while i<len(options_list[index]):
        print(i+1,options_list[index][i])
        i+=1
    user=int(input("enter the number"))
    if user==solution_list[index]:
        return(True)
    else:
        return(False)
def num():
    j=0
    while j<len(question_list):
        print("q",j+1,question_list[j])
        result=function(j)
        if result==True:
            print("congratulation,you got the correct answer")
        else:
            print("you got the wrong answer")
            break
        j+=1
def main():
    num()
main()
        
    