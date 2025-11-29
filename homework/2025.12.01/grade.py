print("q - leütésével kiléphet!")

input_v = ""
while input_v.lower() != 'q':
    input_v = input("Kérek egy számot 1 és 7 között: ")
    if input_v.lower() != "q":
        num = int(input_v)
    match num:
        case 1:
            print("elégtelen")
        case 2:
            print("elégséges")
        case 3:
            print("közepes")
        case 4:
            print("jó")
        case 5:
            print("jeles")
        case _:
            print("1 és 5 között adj meg számokat!")