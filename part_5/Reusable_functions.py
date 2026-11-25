from data.Students import students

#Question 15
def filter_by_track(students, track):
    return [student for student in students if student["track"] == track]


print(filter_by_track(students, "AI"))
print(filter_by_track(students, "Data"))

#Question 16
def average_score(students):
    scores = student["scores"] for student in students
    return sum(scores) / len(scores)

print(average_score(students))


#Question 17
def top_student(students):
    best_student = max(students, key=average_score)
    return best_student["name"]


print(top_student(students))

#Question 18
def summary(students):
    return {
        "total_students": len(students),
        "average_age": round(
            sum(student["age"] for student in students) / len(students), 2
        ),
        "tracks": {student["track"] for student in students}
    }


print(summary(students))
