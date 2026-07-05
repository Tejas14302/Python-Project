def create_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "x"):
            pass
        print("File created successfully!")
    except FileExistsError:
        print("File already exists!")


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(filename, "w") as f:
        f.write(data)
    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as f:
            content = f.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found!")


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(filename, "a") as f:
        f.write(data)
    print("Data appended successfully!")


def file_operations_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                create_file()
            case 2:
                write_file()
            case 3:
                read_file()
            case 4:
                append_file()
            case 5:
                break
            case _:
                print("Invalid choice. Please try again.")
        print("=" * 29)


if __name__ == "__main__":
    file_operations_menu()
