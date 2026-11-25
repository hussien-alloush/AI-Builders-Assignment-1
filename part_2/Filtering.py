from data.Students import students

#Question 4
ai_students = []
for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

print(len(ai_students))

#Question 5
ai_students_Comprehension = [student for student in students if student["track"] == "AI"]
print(ai_students_Comprehension)

#Question 6
students_over_30_hours = [student["name"] for student in students if student["hours_studied"] > 30]
print(students_over_30_hours)

#Question 7
ai_students_over_24 = [student for student in students if student["age"] > 24 and student["track"] == "AI"]
print(ai_students_over_24)
