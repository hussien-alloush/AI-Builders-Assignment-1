from data.students import students

def report(students, min_hours):

    # Step 1: Filter
    filtered = [
        s for s in students
        if s["hours_studied"] >= min_hours
    ]

    # Step 2: Transform and aggregate
    results = [
        {
            "name": s["name"],
            "average_score": average_score(s)
        }
        for s in filtered
    ]

    # Step 3: Sort
    results.sort(
        key=lambda s: s["average_score"],
        reverse=True
    )

    # Step 4: Round scores for presentation
    for result in results:
        result["average_score"] = round(result["average_score"], 1)

    return results


print(report(students, 30))