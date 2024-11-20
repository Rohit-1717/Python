password = "Pas12345jbhbjbkj"

if (len(password)) < 6:
    print("Password is Weak")
elif (len(password)) <= 10 :
    print("Password is medium")
elif (len(password)) > 10:
    print("Password is strong")
exit()