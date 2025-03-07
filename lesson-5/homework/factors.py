import math

def factors(n: int):
    """Returns a sorted list of factors of n."""
    f = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            f.append(i)
            if i != n // i:  # Avoid duplicates (e.g., for perfect squares)
                f.append(n // i)
    return sorted(f)  # Sort the factors before returning

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            fac = factors(num)
            for x in fac:
                print(f"{x} is a factor of {num}")
    except ValueError: #catch in case of invalid input
        print("Invalid input! Please enter a positive integer.")
