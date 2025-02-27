word = input("Enter a word: ")
word = word.lower()
pal = word[::-1]
if pal == word:
    print("palindrome")
else:
    print("not palindrome")