# student_management.py

FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("Student added successfully!")

def view_students():
    try:
        with open(FILE_NAME, "r") as f:
            print("\nRoll | Name | Marks")
            print("-" * 25)
            for line in f:
                roll, name, marks = line.strip().split(",")
                print(f"{roll} | {name} | {marks}")
    except FileNotFoundError:
        print("No records found.")

def search_student():
    roll_search = input("Enter Roll No to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                if roll == roll_search:
                    print(f"Found: {roll} | {name} | {marks}")
                    found = True
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        print("\n1.Add Student\n2.View Students\n3.Search Student\n4.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

main()
