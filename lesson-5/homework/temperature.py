def convert_cel_to_far(c): #c temperature in Celsius
    return c * 9 / 5 + 32 #use the formula to convert into Fahrenheit
def convert_far_to_cel(f): #f - temp in Fahrenheit
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    try:
        in1 = float(input("Enter a temperature in degrees F: "))
        f = convert_far_to_cel(in1)
        print(f"{in1} degrees F = {f:.2f} degrees C")

        in2 = float(input("Enter a temperature in degrees C: "))
        c = convert_cel_to_far(in2)
        print(f"{in2} degrees C = {c:.2f} degrees F")
    except ValueError:
        print("Invalid input!")