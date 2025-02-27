str1 = input("Enter a string: ")
str1 = str1.lower()
vowel = 0
consonant = 0
for char in str1:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel+=1
    else:
        consonant+=1
print(f"vowel count: {vowel} and consonant count: {consonant}")