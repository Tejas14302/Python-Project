import random
import string


def generate_random_number():
    try:
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        if low > high:
            low, high = high, low
        print(f"Random Number: {random.randint(low, high)}")
    except ValueError:
        print("Please enter valid whole numbers.")


def generate_random_list():
    try:
        count = int(input("Enter number of elements: "))
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        if low > high:
            low, high = high, low
        result = [random.randint(low, high) for _ in range(count)]
        print(f"Random List: {result}")
    except ValueError:
        print("Please enter valid whole numbers.")


def create_random_password():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid whole number.")


def generate_random_otp():
    otp = "".join(random.choice(string.digits) for _ in range(6))
    print(f"Generated OTP: {otp}")


def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                generate_random_number()
            case 2:
                generate_random_list()
            case 3:
                create_random_password()
            case 4:
                generate_random_otp()
            case 5:
                break
            case _:    
                print("Invalid choice. Please try again.")
        print("=" * 29)


if __name__ == "__main__":
    random_menu()
