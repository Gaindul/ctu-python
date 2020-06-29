'''
With this assignment, you will be taking user input for someone’s name, age, and a password. You will first
take the password the user gave and verify this is correct. For this, use an if-statement to see if the input
string is equal to the password. You can set this password to whatever you would like.
Once the user’s password that they entered has been verified, continue onto the next step. You will take
their age and perform some checks. We are going to consider 3 criteras. Whether the user can vote, drink,
and drive.
• You can drive if you are 16 years or older.
• You can vote if you are 18 years or older.
• You can drink if you are 21 years or older
'''
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