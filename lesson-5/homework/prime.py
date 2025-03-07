def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3): #prime
        return True
    if num % 2 == 0 or num % 3 == 0: #exclude multiples of 2 and 3
        return False
    #check for numbers of the form 6k+1 or 6k-1
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0: # i = 6k-1 ; i+2 = 6k+1
            return False
    return True

if __name__ == "__main__":
    try:
        print(is_prime(int(input("Enter a number: "))))
    except ValueError: print("Invalid input!")
