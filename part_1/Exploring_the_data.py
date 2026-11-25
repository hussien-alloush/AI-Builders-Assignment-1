from data.Students import students

#Question 1
print(students[0]["name"])  # Output: Lara
print(students[1]["name"])   # Output: sami

#Question 2
for student in students:
    if student["name"] == "Rim":
        print(student["scores"])
        break

#Question 3
for student in students:
    print(f"{student['name']} is {student['age']} years old and studies {student['track']}")