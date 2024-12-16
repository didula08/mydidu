#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
    return float(a)+float(b)
    
def subtract(a,b):
    return float(a)-float(b)
    
def multiply(a,b):
    return float(a)*float(b)
    
def devide(a,b):
    if float(b)!=0:
        return float(a)/float(b)
    else:
        return "float division by zero"

def power(a,b):
    return float(a)**float(b)
    
def remainder(a,b):
    return float(a)%float(b)

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice=='#':
        return -1;
        
    elif (choice in ('+','-','*','/','^','%','#')):
        while True:
            firstnum=str(input("Enter first number: "))
            print(firstnum)
            if  firstnum.endswith('$'):
                return 0;
            if firstnum.endswith('#'):
                return -1;
            
            try:
                num1=float(firstnum)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        while True:
            secondnum=str(input("Enter second number: "))
            print(secondnum)
            if secondnum.endswith('$'):
                return 0;
            if secondnum.endswith('#'):
                return -1;
            
            try:
                num2=float(secondnum)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        
        if choice=='+':
            print(num1,'+',num2,'=',add(num1,num2))
            
        elif choice=='-':
            print(num1,'-',num2,'=',subtract(num1,num2))
            
        elif choice=='*':
            print(num1,'*',num2,'=',multiply(num1,num2))
        
        elif choice=='/':
            if num2!=0:
                print(num1,'/',num2,'=',devide(num1,num2))
            else:
                print(devide(num1,num2))
                print(num1,'/',num2,'=',None)
            
        elif choice=='^':
            print(num1,'^',num2,'=',power(num1,num2))
            
        elif choice=='%':
            print(num1,'%',num2,'=',remainder(num1,num2))
            
        else:
            print("Unrecognized operation")
    
    else:
        print("Something Went Wrong")




#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()