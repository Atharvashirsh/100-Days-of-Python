names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

import random

students_scores = {student: random.randint(0, 100) for student in names}
print(students_scores)

passed_students = {
    student: marks for (student, marks) in students_scores.items() if marks > 30
}
print(passed_students)
