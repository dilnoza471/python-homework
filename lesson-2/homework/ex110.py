str1 = input("Enter a sentence: ")
str1 = str1.strip()
num = 0
for word in str1.split(' '):
    if word:
        num += 1
print(f"It has {num} words")

