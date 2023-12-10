gradebook = {
    "Alice": {"Math": 90, "Science": 95, "English": 85},
    "Bob": {"Math": 80, "Science": 88, "English": 89},
    "David": {},
}


def add_grade(student_name: str, subject: str, grade: int) -> None:
    student_exists = student_name in gradebook
    if student_exists:
        gradebook[student_name][subject] = grade

    if not student_exists:
        print(f"Student {student_name} does not exist.")


def calculate_average(student_name: str) -> int:
    average = None

    student_exists = student_name in gradebook
    if student_exists:
        student_grades = gradebook[student_name].values()

        if student_grades:  # Check if there are grades to avoid division by zero
            average = sum(student_grades) / len(student_grades)
        else:
            print(f"Student {student_name} has no grades.")

    if not student_exists:
        print(f'Student {student_name} does not exist.')

    return average


print(f"Alice: {calculate_average('Alice')}\n")
print(f"Bob: {calculate_average('Bob')}\n")
print(f"Charlie: {calculate_average('Charlie')}\n")
print(f"David: {calculate_average('David')}\n")  # This will raise a ZeroDivisionError
