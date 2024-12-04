while True:
    number = int(input("Enter Value between 1 and 10: "))
    
    if 1 <= number <= 10:
        print("Thanks :)")
        break
    else:
        print("Invalid Number, try again")