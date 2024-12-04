table_Number = int(input("Enter the number you want the table for : "))

for i in range(1,11):
    if i == 5:
        continue
    print(table_Number, 'X' , i , '=' , table_Number * i)