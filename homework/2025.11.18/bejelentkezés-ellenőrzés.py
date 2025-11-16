users = {
    'admin': '1234',
    'user': 'abcd'
}

username = input("Felhasználónév: ")

if username in users:
    password = input("Jelszó: ")

    if users[username] == password:
        print("Bejelentkezés sikeres!")
    else:
        print("Hibás jelszó!")

else:
    print("Nincs ilyen felhasználó!")