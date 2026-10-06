students = {"Vivaan": {"Math": 85, "Science": 90, "English": 78},
            "Aanay": {"Math": 92, "Science": 88, "English": 65},
            "Aden": {"Math": 85, "Science": 80, "English": 90},
            "Billy": {"Math": 55, "Science": 78, "English": 70}}

student_names1 = list(students.keys())
print("List of students:")
for name in student_names1:
    print(f"  {name}")
    print()

for student, grades in students.items():
    total_score = sum(grades.values())
    average_score = total_score / len(grades)
    print(f"{student}'s average score is: {average_score:.2f}")
    print()

student_min = min(students, key=lambda student: sum(students[student].values()))
print(f"The student with the lowest total score is: {student_min}")
student_max = max(students, key=lambda student: sum(students[student].values()))
print(f"The student with the highest total score is: {student_max}\n")

student_name = input("Enter the name of the student to view their grades: ")
if student_name in students:
    print(f"{student_name}'s grades:")
    for subject, grade in students[student_name].items():
        print(f"  {subject}: {grade}")
else:
    print("Student not found.")