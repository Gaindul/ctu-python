color1 = input("Enter the first color: ")
color2 = input("Enter the second color: ")
color3 = input("Enter the third color: ")
color4 = input("Enter the fourth color: ")

colors = []
colors.append(color1)
colors.append(color2)
colors.append(color3)
colors.append(color4)

print(len(colors)) 
if len(colors)==4:
    colors.append("Black")
    colors.pop()
if colors[0]=="Red":
    print("The first color you thought of was red!")
elif colors[0]=="Green":
    print("Eww, your first choice was green?!")