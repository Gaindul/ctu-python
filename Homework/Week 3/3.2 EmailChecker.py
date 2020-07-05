Input=input("Enter an email address: ").lower()
GmailPresent="@gmail.com" in Input
if GmailPresent==True:
    print("The Domain is Correct!")
else:
    print("The Domain is Incorrect!")