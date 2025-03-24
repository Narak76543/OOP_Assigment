class StudentManagement:
   
    def __init__(self, filename):
        self.filename = filename
    
    def create(self):
        # Gather student information, including the new fields
        student_id = input("Enter student ID: ")
        first_name = input("Enter student First Name: ")
        last_name = input("Enter student Last Name: ")
        age = input("Enter student Age: ")
        department = input("Enter student Department: ")

        # Check if age is a number
        if not age.isdigit():
            print("Error: Age must be a number.") 
            return  

        # Open the file in append mode ('a') to add new data without overwriting existing data
        with open(self.filename, 'a') as file:
            file.write(f"{student_id},{first_name},{last_name},{age},{department}\n")

        print(f"Student '{first_name} {last_name}' added successfully.")

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    print("Student Information:")

                    for line in lines:
                        student_data = line.strip().split(",")
                        print(f"ID: {student_data[0]}, First Name: {student_data[1]}, Last Name: {student_data[2]}, Age: {student_data[3]}, Department: {student_data[4]}")
                else:
                    print("No student data found.")
        except FileNotFoundError:
            print("File not found. No data to read.")

    def update(self, student_id, new_first_name=None, new_last_name=None, new_age=None, new_department=None):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            with open(self.filename, 'w') as file:
                updated = False  

                for line in lines:
                    student_data = line.strip().split(",")
                    
                    if student_data[0] == student_id:
                        # Update fields if new data is provided
                        if new_first_name:
                            student_data[1] = new_first_name

                        if new_last_name:
                            student_data[2] = new_last_name

                        if new_age:
                            student_data[3] = new_age
                            
                        if new_department:
                            student_data[4] = new_department

                        # Write the updated student data back to the file
                        file.write(",".join(student_data) + "\n")
                        updated = True  
                    else:
                        file.write(line)
                
                if updated:
                    print(f"Student ID '{student_id}' updated successfully.")
                else:
                    print(f"Student ID '{student_id}' not found.")
        except FileNotFoundError:
            print("File not found. No data to update.")

    def delete(self, student_id):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            with open(self.filename, 'w') as file:
                deleted = False  # Flag to check if any deletion has been made
                for line in lines:
                    student_data = line.strip().split(",")
                    if student_data[0] != student_id:
                        file.write(line)
                    else:
                        deleted = True  

                if deleted:
                    print(f"Student ID '{student_id}' deleted successfully.")
                else:
                    print(f"Student ID '{student_id}' not found.")
        except FileNotFoundError:
            print("File not found. No data to delete.")

# Main program execution starts here
if __name__ == "__main__":

    filename = "students.txt"
    student_manager = StudentManagement(filename)

    # Infinite loop to display the menu 
    while True:
        # Display the menu options
        print("\n--- CRUD Operations on Student's Information ---")
        print("1. Register")
        print("2. View All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':  
                student_manager.create()
            case '2': 
                student_manager.read()
            case '3':  
                student_id = input("Enter student ID to update: ")
                new_first_name = input("Enter new First Name (or press Enter to skip): ")
                new_last_name = input("Enter new Last Name (or press Enter to skip): ")
                new_age = input("Enter new Age (or press Enter to skip): ")
                new_department = input("Enter new Department (or press Enter to skip): ")
               # Simplified update method call
                student_manager.update(
                                        student_id, 
                                        new_first_name or None, 
                                        new_last_name or None, 
                                        new_age or None, 
                                        new_department or None)


            case '4':  
                student_id = input("Enter student ID to delete: ")
                student_manager.delete(student_id)
            case '5':  
                print("Exiting the system. Goodbye!")
                break
            case _: 
                print("Invalid choice. Please try again.")
