import math

# Function to add two numbers  
def addThem(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtractThem(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiplyThem(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divideThem(num1, num2): 
    return num1 / num2 

    # Take input from the user  
def user_input():
            while True:                
                number_1 = input("Enter first number: ")
                number_2 = input("Enter second number: ") 
                numbers = number_1 + number_2

                if not numbers.isdigit():
                    print("Wrong input, >:(, Try again!\n")
                    continue     
 

                num1 = int(number_1)
                num2 = int(number_2)          
                
                print('\nResults:\n')
                print(num1,"Plus",num2,"Equals",addThem(num1, num2))
                print(num1,"Minus",num2,"Equals",subtractThem(num1, num2))
                print(num1,"Multiplied",num2,"Equals",multiplyThem(num1, num2))
                print(num1,"Divided By",num2,"Equals",divideThem(num1, num2))
                print('\n')
                return(user_input())
                        

run = user_input()
     