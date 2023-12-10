# TODO 🏠: - Identify the cause of the exception by following these steps:
#   1. Run the script.
#   2. Set debugger breakpoints on any line numbers mentioned in the exception
#      message you should receive.
#   3. Run the debugger.
#   4. Traverse through the breakpoints until you arrive at the line that the
#       error occurs.
#   4. Run the line of code causing the error in Debugger terminal to
#      replicate and isolate the issue.
#   5. Break down the problematic line into its components, such as variables,
#      and execute them in the debugger terminal. This will isolate the error
#      even further help identify why the error is occurring.
#   Once you have isolated the error and understand the exact reason behind it,
#   proceed with implementing a fix:
#   - Wrap the problematic line within an `if` statement, addressing the
#     specific scenario that triggers the error. Consider using `else` or
#     `if not` as necessary to cover alternate cases.

gradebook = {
    "Alice": { "Math": 90, "Science": 95, "English": 85 },
    "Bob": { "Math": 80, "Science": 88, "English": 89 },
    "David": { },
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
        average = sum(student_grades) / len(student_grades)

    if not student_exists:
        print(f'Student {student_name} does not exist.')

    return average


print(f"Alice: {calculate_average('Alice')}\n")
print(f"Bob: {calculate_average('Bob')}\n")
print(f"Charlie: {calculate_average('Charlie')}\n")
print(f"David: {calculate_average('David')}\n")  # This will raise a ZeroDivisionError
