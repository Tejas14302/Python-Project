student_records = {}  
offered_subjects = set()  
print("Welcome to the Student Data Organizer!")
while True:
    print("\nSelect an option:")
    print("Press 1 To Add Student")
    print("Press 2 To Display All Students")
    print("Press 3 To Update Student Information")
    print("Press 4 To Delete Student")
    print("Press 5 To Display Subjects Offered")
    print("Press 6 To Exit")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = int(input("Age: ")) 
            grade = input("Grade: ")
            dob = input("Date of Birth: ")
            subjects_input = input("Subjects (Comma Separated): ")
            subjects_list = [s.strip() for s in subjects_input.split(',')]
            offered_subjects.update(subjects_list)
            id_dob_tuple = (student_id, dob)
            student_records[student_id] = {"id_dob": id_dob_tuple,"name": name,"age": age,"grade": grade,"subjects": subjects_list}
            print("\nStudent added successfully!")
        case '2':
            print("\nDisplay All Students")
            if not student_records:
                print("No students found.")
            else:
                for s_id, info in student_records.items():
                    subs = ", ".join(info['subjects'])
                    print(f"Student ID: {s_id} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']} | Subjects: {subs}")
        case '3':
            print("\nUpdate Student Information")
            s_id = input("Enter Student ID to update: ")
            if s_id in student_records:
                print("Leave blank to keep the current values.")
                new_name = input(f"Name ({student_records[s_id]['name']}): ")
                if new_name: 
                    student_records[s_id]['name'] = new_name
                new_age = input(f"Age ({student_records[s_id]['age']}): ")
                if new_age: 
                    student_records[s_id]['age'] = int(new_age)
                new_grade = input(f"Grade ({student_records[s_id]['grade']}): ")
                if new_grade: 
                    student_records[s_id]['grade'] = new_grade
                print("Student updated successfully!")
            else:
                print("Student ID not found.")

        case '4':
            print("\nDelete Student")
            s_id = input("Enter Student ID to delete: ")
            if s_id in student_records:
                student_records.pop(s_id) 
                print(f"Student {s_id} deleted successfully.")
            else:
                print("Student ID not found.")
        case '5':
            print("\n--- Subjects Offered ---")
            if offered_subjects:
                print(", ".join(offered_subjects))
            else:
                print("No subjects added yet.")
        case '6':
            print("\nThank you for using the Student Data Organizer. Goodbye!")
            break  
        case _:
            print("\nInvalid choice. Please select a valid option (1-6).")