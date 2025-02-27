str1 = input("Input sentence:")
rep = input("Replace : ")
an = input("With: ")
if rep in str1:
    str2 = str1.replace(rep,an)
    print(str2)
else:
    print("Invalid input")