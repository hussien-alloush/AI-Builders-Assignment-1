from data.Students import students

#Question 8
average_age = sum(s["age"] for s in students) / len(students)

print(round(average_age, 2))

#Question 9
total_hours = sum(s["hours_studied"] for s in students)

print(total_hours)

#Question 10
most_studied = students[0]

for student in students:
    if student["hours_studied"] > most_studied["hours_studied"]:
        most_studied = student

print(most_studied["name"])
print(most_studied["hours_studied"])

#Question 11
for student in students:
    grade = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {grade:.1f}")
