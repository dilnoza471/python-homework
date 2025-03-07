def invest(amount, rate, years):
    for i in range(years):
        amount *= (1+rate) #add 1 to calculate the new amount
        print(f"year {i+1}: ${amount:.2f}")
if __name__ == "__main__":
    try:
        base = float(input("Initial amount: "))
        if base <= 0:
            print("Invalid input!")
            exit(1)
        r = float(input(" rate of interest: "))
        if r <= 0:
            print("Invalid input!")
            exit(1)
        year = int(input("Enter years: "))
        if year <= 0:
            print("Invalid input!")
            exit(1)
        invest(base, r, year)
    except ValueError:
        print("Invalid input!")