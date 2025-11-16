grades = {"anna": 75, "béla": 45, "csaba": 90}

name = input("Addj meg egy nevet: ")
if name.lower() in grades.keys() and grades[name] > 50:
    print("Sikeres vizsga.")
elif name.lower() in grades.keys() and grades[name] < 50:
    print("Sikertelen vizsga.")
elif name.lower() not in grades.keys():
    print("Nincs ilyen diák.")