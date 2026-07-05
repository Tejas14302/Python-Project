from Modules import datetime_time_ops
from Modules import math_ops
from Modules import random_ops
from Modules import uuid_ops
from Modules import file_operations_menu


def explore_module_attributes():
    print("Explore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    try:
        module = __import__(module_name)
        attributes = dir(module)
        print(f"Available Attributes in {module_name} module:")
        print(attributes)
    except ImportError:
        print(f"Module '{module_name}' not found!")


def display_main_menu():
    print("=" * 29)
    print("Welcome to Multi-Utility Toolkit")
    print("=" * 29)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 29)


def main_menu():
    while True:
        display_main_menu()
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                datetime_time_ops.datetime_menu()
            case 2:
                math_ops.math_menu()
            case 3:
                random_ops.random_menu()
            case 4:
                uuid_ops.generate_unique_identifier()
                print("=" * 29)
            case 5:
                file_operations_menu()
            case 6:
                explore_module_attributes()
                print("=" * 29)
            case 7:
                print("=" * 29)
                print("Thank you for using the Multi-Utility Toolkit!")
                print("=" * 29)
                break
            case _:    
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
