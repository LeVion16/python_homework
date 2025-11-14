grades = {
    "matek": 4,
    "töri": 3,
    "informatika": 5,
    "fizika": 2
}

def best_grade(grades: dict) -> str:
    if not grades:
        return None


    """ max() verzió (toggle block kommentben)
        best = max(grades, key=grades.get)
        return best """

    best = None
    best_value = 0
    for subject in grades:
        grade = grades[subject]   
        if grade > best_value:
            best = subject
            best_value = grade
    return best

print(best_grade(grades))