import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename=("journal.txt")):
        self.filename=filename

    def add_entry(self,entry):
        try:
            time=datetime.now().strftime("[%Y-%M-%D %H:%M:%S]")
            with open(self.filename, "a") as f:
                f.write(f"{time}\n{entry}\n\n")
            print("\nEntry added successfully!")
            print()
        except PermissionError:
            print("Error: Permission denied. cannot write Journal file!")

        except Exception as e:
            print(f"Unexpected Error Occured:{e}")

    def view_entries(self):
        try:
            with open(self.filename, "r") as f:
                content=f.read().strip()
            if content:
                print("Your Journal Entries:")
                print("-"*30)
                print(content)
                print()
            else:
                print("No Journal Entries found!!")
                print()
        except FileNotFoundError:
            print("No Journal Entries found!!")
            print()
        
        except PermissionError:
            print("Error: Permission denied. cannot Read Journal file!")
            print()
            
        except Exception as e:
            print(f"Unexpected Error Occured:{e}")
            print()

    def search_entry(self,search):
        try:
            with open(self.filename , "r") as f:
                content= f.read().strip()

            entries= content.split("\n\n")
            matches=[e for e in entries if search.lower() in e.lower() and e.strip()]
            if matches:
                print("Matching Entries:")
                print("-"*30)
                for m in matches:
                    print(m.strip())
                    print()
            else:
                print("No Entries found!!")

        except FileNotFoundError:
            print("No Journal Entries found!!")
            print()
        
        except PermissionError:
            print("Error: Permission denied. cannot Read Journal file!")
            print()
            
        except Exception as e:
            print(f"Unexpected Error Occured:{e}")
            print()

    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("No journal entries to Delete.\n")
                return
            
            confirm=input("Rre you sure you want to delete all journal(Yes/no):")
            print()

            if confirm=="Yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")
        
        except PermissionError:
            print("Error: Permission denied. cannot delete Journal file!")
            
        except Exception as e:
            print(f"Unexpected Error Occured:{e}")



manager=JournalManager()
print("Welcome to Personal Journal Manager!")
print()

while True:
    print("please Select an option:")
    print()
    print("Press 1 to Add a New Entry.")
    print("Press 2 to View all Entries.")
    print("Press 3 to Search for Entry.")
    print("Press 4 to Delete all Entry.")
    print("Press 5 to Exit.")
    print()
    choice=int(input("User input: ").strip())
    print()

    match choice:
        case 1:
            entry=input("Enter Your journal entry:\n").strip()
            manager.add_entry(entry)
        case 2:
            manager.view_entries()
        case 3:
            search=input("Enter Keyword or Date to found: ").strip()
            manager.search_entry(search)
        case 4:
            manager.delete_entries()
        case 5:
            print("Thank you for using Personal journal Manager. Goodbye!!")
            print()
            break
        case _:
            print("Invalid choice!!!!")
