from data.Students import students

#Question 12
student_results = [
    {
        "name": student["name"],
        "average_score": round(sum(student["scores"]) / len(student["scores"]), 1)
    }
    for student in students
]

print(student_results)

#Question 13
track_counts = {}

for student in students:
    track = student["track"]
    track_counts[track] = track_counts.get(track, 0) + 1

print(track_counts)


#Question 14

unique_tracks = {student["track"] for student in students}
print(unique_tracks)



