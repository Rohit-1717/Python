input_str = str(input("Enter the word in which you want to check the non-repeated character : "))

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Character is: ",char)
        break
        