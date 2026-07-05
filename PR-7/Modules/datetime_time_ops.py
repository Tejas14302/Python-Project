import datetime
import time


def display_current_datetime():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_date_difference():
    try:
        first = input("Enter the first date (YYYY-MM-DD): ")
        second = input("Enter the second date (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(second, "%Y-%m-%d")
        difference = abs((date2 - date1).days)
        print(f"Difference: {difference} days")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")


def format_custom_date():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        fmt = input("Enter desired format (e.g., %d-%m-%Y, %B %d, %Y): ")
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        print(f"Formatted Date: {date_obj.strftime(fmt)}")
    except ValueError:
        print("Invalid date or format string!")


def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Elapsed Time: {elapsed:.2f} seconds")


def countdown_timer():
    try:
        seconds = int(input("Enter countdown time (in seconds): "))
        while seconds >= 0:
            print(f"Time remaining: {seconds} seconds")
            time.sleep(1)
            seconds -= 1
        print("Time's up!")
    except ValueError:
        print("Please enter a valid whole number of seconds.")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                display_current_datetime()
            case 2:
                calculate_date_difference()
            case 3:
                format_custom_date()
            case 4:
                stopwatch()
            case 5:
                countdown_timer()
            case 6:
                break
            case _:
                print("Invalid choice. Please try again.")
        print("=" * 29)


if __name__ == "__main__":
    datetime_menu()
