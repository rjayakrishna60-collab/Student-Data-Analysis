students = []

def add_student():
    name = input("Enter student name: ")
    marks1 = int(input("Maths marks: "))
    marks2 = int(input("Science marks: "))
    marks3 = int(input("English marks: "))

    avg = (marks1 + marks2 + marks3) / 3

    student = {
        "name": name,
        "average": avg
    }

    students.append(student)
    print("Student added successfully!\n")


def show_students():
    if not students:
        print("No data available\n")
        return

    for s in students:
        print(f"Name: {s['name']} | Average: {s['average']}")


def show_topper():
    if not students:
        print("No data available\n")
        return

    topper = max(students, key=lambda x: x['average'])
    print(f"\nTopper: {topper['name']} with {topper['average']} marks\n")


while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Show Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        show_topper()
    elif choice == '4':
        break
    else:
        print("Invalid choice")