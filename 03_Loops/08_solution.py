number = int(input("Enter the number you want to check for prime number : "))

is_Prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_Prime = False
            break

print(is_Prime)
