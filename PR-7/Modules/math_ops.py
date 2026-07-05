import math


def calculate_factorial():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers!")
            return
        print(f"Factorial: {math.factorial(num)}")
    except ValueError:
        print("Please enter a valid whole number.")


def solve_compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time_years = float(input("Enter time (in years): "))
        amount = principal * (1 + rate / 100) ** time_years
        print(f"Compound Interest: {amount:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")


def trigonometric_calculations():
    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)
        print(f"sin({angle}) = {math.sin(radians):.4f}")
        print(f"cos({angle}) = {math.cos(radians):.4f}")
        print(f"tan({angle}) = {math.tan(radians):.4f}")
    except ValueError:
        print("Please enter a valid numeric angle.")


def area_of_shapes():
    print("Choose a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    choice = int(input("Enter your choice: "))

    try:
        match choice:
            case 1:
                radius = float(input("Enter radius: "))
                print(f"Area of Circle: {math.pi * radius ** 2:.2f}")
            case 2:
                side = float(input("Enter side length: "))
                print(f"Area of Square: {side ** 2:.2f}")
            case 3:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"Area of Rectangle: {length * width:.2f}")
            case 4:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area of Triangle: {0.5 * base * height:.2f}")
            case _:
                print("Invalid choice.")
    except ValueError:
        print("Please enter valid numeric values.")


def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                calculate_factorial()
            case 2:
                solve_compound_interest()
            case 3:
                trigonometric_calculations()
            case 4:
                area_of_shapes()
            case 5:
                break
            case _:
                print("Invalid choice. Please try again.")
        print("=" * 29)


if __name__ == "__main__":
    math_menu()
