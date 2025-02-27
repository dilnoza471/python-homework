txt = input("Input: ")
word = True
txt1 = ''
for char in txt:
    if char == ' ':
        word = True
    elif word:
        txt1 += char
        word = False

print(txt1)