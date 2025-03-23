class StudentManagement:
    def __init__(self, filename):
        self.filename = filename

    # Create operation: Add a new student with user input
    def create(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student Name: ")
        age = input("Enter student Age: ")

        # Validate input (basic check for age to be a number)
        if not age.isdigit():
            print("Error: Age must be a number.")
            return

        # Save the student data into the file
        with open(self.filename, 'a') as file:
            file.write(f"{student_id},{name},{age}\n")
        print(f"Student '{name}' added successfully.")

    # Read operation: Display all students
    def read(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    print("Student Information:")
                    for line in lines:
                        student_data = line.strip().split(",")
                        print(f"ID: {student_data[0]}, Name: {student_data[1]}, Age: {student_data[2]}")
                else:
                    print("No student data found.")
        except FileNotFoundError:
            print("File not found. No data to read.")

    # Update operation: Update a student's information
    def update(self, student_id, new_name=None, new_age=None):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            with open(self.filename, 'w') as file:
                updated = False
                for line in lines:
                    student_data = line.strip().split(",")
                    if student_data[0] == student_id:
                        if new_name:
                            student_data[1] = new_name
                        if new_age:
                            student_data[2] = new_age
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

    # Delete operation: Delete a student by ID
    def delete(self, student_id):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            with open(self.filename, 'w') as file:
                deleted = False
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


# Example usage:
if __name__ == "__main__":
    # File where student data will be stored
    filename = "students.txt"

    # Create student management object
    student_manager = StudentManagement(filename)

    # Main menu loop to interact with the student management system
    while True:
        print("\n--- Student Management System ---")
        print("1. Create Student")
        print("2. View All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            student_manager.create()  # Create a new student by input
        elif choice == '2':
            student_manager.read()  # Display all students
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            new_name = input("Enter new Name (or press Enter to skip): ")
            new_age = input("Enter new Age (or press Enter to skip): ")

            # Update only if there's new data provided
            student_manager.update(student_id, new_name if new_name else None, new_age if new_age else None)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            student_manager.delete(student_id)  # Delete student by ID
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
