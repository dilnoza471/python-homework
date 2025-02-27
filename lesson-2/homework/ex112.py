n = int(input("Enter the number of words to join: "))
txt = ""

for _ in range(n):
    txt += f"{input("word: ")}, "
txt = txt[:-2]
print(txt)
