# Student Result Management System
# Simple Python program to manage students and calculate grades

import json

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = {}
    subjects = ["Maths", "Science", "English"]

    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks[sub] = m

    total = sum(marks.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student data available.\n")
        return

    for s in students:
        print("--------------------------------------")
        print(f"Name: {s['name']}")
        print(f"Roll No: {s['roll']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")
    print("--------------------------------------\n")

def save_data():
    with open('students_data.json', 'w') as f:
        json.dump(students, f, indent=4)
    print("Data saved successfully!\n")

def load_data():
    global students
    try:
        with open('students_data.json', 'r') as f:
            students = json.load(f)
        print("Data loaded successfully!\n")
    except FileNotFoundError:
        print("No saved data found. Starting fresh...\n")

def main():
    load_data()

    while True:
        print("===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Save Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            save_data()
        elif choice == '4':
            save_data()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
