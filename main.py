# Student Management System

students = []


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "phone": phone
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    print("\n--- All Students ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
        print("Phone  :", student["phone"])


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Phone  :", student["phone"])
            return

    print("Student not found!")


def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Leave blank if you don't want to change a field.")

            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")
            phone = input("Enter New Phone: ")

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if course:
                student["course"] = course

            if phone:
                student["phone"] = phone

            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")

    def delete_student():
     print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():
    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
            main()
 