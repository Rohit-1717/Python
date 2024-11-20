year = 2024

if (year % 400 == 0) or (year % 4 == 0  and year % 100 != 0):
    print(year, " is a leap Year")
else:
    print(year, " is NOT leap Year")
exit ()