from app.manager import StudentManager


def show_menu():
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                student_id = input("Student ID: ")
                name = input("Name: ")
                age = int(input("Age: "))
                course = input("Course: ")

                manager.add_student(student_id, name, age, course)
                print("✅ Student added successfully")

            elif choice == "2":
                students = manager.view_students()
                if not students:
                    print("No students found")
                for s in students:
                    print(s)

            elif choice == "3":
                student_id = input("Enter Student ID to delete: ")
                manager.delete_student(student_id)
                print("🗑️ Student deleted successfully")

            elif choice == "4":
                print("Exiting program...")
                break

            else:
                print("❌ Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
