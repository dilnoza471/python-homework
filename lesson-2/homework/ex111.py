txt = input("Enter a string: ")
if any(char.isdigit() for char in txt):
    print("Contains digits")
else:
    print("No digits")