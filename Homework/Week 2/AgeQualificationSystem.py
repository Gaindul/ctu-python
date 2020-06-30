FirstName=input("Please enter your first name: ")
LastName=input("Please enter your last name: ")
Age=int(input ("Please enter your age: "))

PasswordEntry=input("Please enter the password: ")
Password="password123"
if PasswordEntry==Password:
    if 18>Age>16:
        print("Hello", FirstName, LastName, "! You are", Age, "and are allowed to drive")
    elif 21>Age>18:
        print("Hello", FirstName, LastName, "! You are", Age, "and are allowed to drive and vote")
    elif Age>21:
        print("Hello", FirstName, LastName, "! You are", Age, "and are allowed to drive, vote and drink")
else:
    print("Password is incorrect")