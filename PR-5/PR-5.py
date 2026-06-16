class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("Person Details:")
        print(f"  Name : {self.name}")
        print(f"  Age  : {self.age}")

    def __del__(self):
        pass

class employee(person):
    def __init__(self, name, age,employee_id,salary):
        super().__init__(name,age)
        self.set_employee_id(employee_id)
        self.set_salary(salary)

    def get_employee_id(self):
        return self.__employee_id
    
    def get_salary(self):
        return self.__salary
    
    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id

    def set_salary(self,salary):
        if salary<0:
            print("Salary cannot be Negative!!!")
            self.__salary=0.0
            return
        self.__salary=salary

    def display(self):
        print(f"Employee Details:")
        print(f"  Name        : {self.name}")
        print(f"  Age         : {self.age}")
        print(f"  Employee ID : {self.__employee_id}")
        print(f"  Salary      : ${self.__salary:.1f}")
    
    def __del__(self):
        pass

class manager(employee):

    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name, age, employee_id, salary)
        self.__department=department

    def get_department(self):
        return self.__department

    def display(self):
        print(f"Manager Details:")
        print(f"  Name        : {self.name}")
        print(f"  Age         : {self.age}")
        print(f"  Employee ID : {self.get_employee_id()}")
        print(f"  Salary      : ${self.get_salary():.1f}")
        print(f"  Department  : {self.__department}")

    def __del__(self):
        pass
def main():
    print("---Python OOP Project: Employee Management System---")
    print()

    created_obj:dict={
        "person" : [],
        "employee" : [],
        "manager" : []
    }

    while True:
        print("Choose a Operation:")
        print("Press 1 to Create a Person")
        print("Press 2 to Create a Employee")
        print("Press 3 to Create a Manager")
        print("Press 4 to Show Details")
        print("Press 5 to Exit")
        print()
        choice=int(input("Enter your Choice:"))
        print()
        match choice:
            case 1:
                name=input("Enter Name: ".strip())
                age=int(input("Enter Age: ").strip())
                p=person(name,age)
                created_obj["person"].append(p)
                print()
                print(f"Person created with Name: {p.name} and age: {p.age}.")
                print()
            case 2:
                name=input("Enter Name: ".strip())
                age=int(input("Enter Age: ").strip())
                emp_id=input("Enter Employee ID: ".strip())
                salary=float(input("Enter Salary: ").strip())
                e=employee(name,age,emp_id,salary)
                created_obj["employee"].append(e)
                print()
                print(f"Employee created with name: {e.name}, age: {e.age}, ID: {e.get_employee_id()}, and salary: ${e.get_salary():.1f}.")
                print()
            case 3:
                name=input("Enter Name: ".strip())
                age=int(input("Enter Age: ").strip())
                emp_id=input("Enter Employee ID: ".strip())
                salary=float(input("Enter Salary: ").strip())
                dept=input("Enter Department: ".strip())
                m=manager(name,age,emp_id,salary,dept)
                created_obj["manager"].append(m)
                print(f"Manager created with name: {m.name}, age: {m.age}, ID: {m.get_employee_id()}, and salary: ${m.get_salary():.1f}, Department: {m.get_department()}.")
                print()
            case 4:
                print("Choose details to Show:")
                print("Press 1 to Show Person.")
                print("Press 2 to Show Employee.")
                print("Press 3 to Show Manager.")
                sub=input("Enter Your Choice: ").strip()
                print()
                mapping={
                    "1": ("person",    "No Person created yet."),
                    "2": ("employee",  "No Employee created yet."),
                    "3": ("manager",   "No Manager created yet."),
                }

                if sub in mapping:
                    key, msg = mapping[sub]
                    objs = created_obj[key]
                    if not objs:
                        print(f"\n{msg}")
                    else:
                        print()
                        for obj in objs:
                            obj.display()
                            print("-"*20)
                        print()
                else:
                    print("Invalid choice.")
            case 5:
                print("Exiting the system. all resources have been Freed.")
                for category in created_obj.values():
                       category.clear()
                break
            case _:
                print("Invalid Choice!!!")
if __name__=="__main__":
    main()