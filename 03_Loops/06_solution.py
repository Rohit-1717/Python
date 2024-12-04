number = int(input("Enter the number for which you want to calculate factorial : "))

factorial = 1

while number > 0 :
    # factorial  = factorial * number
    # number = number - 1
    
    factorial *= number
    number -= 1
    
print("Factorial of the given number is : ",factorial )