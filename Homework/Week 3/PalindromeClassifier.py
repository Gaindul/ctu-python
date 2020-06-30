InputString=input("Enter a string:").lower()
RevString= InputString[:: -1]
if RevString==InputString:
    print(InputString, "is a palindrome!")
else:
    print("Unfortunately",InputString,"is not a palindrome")