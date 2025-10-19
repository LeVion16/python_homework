def is_correct_pwd(p: str) -> bool:
    chars = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
    upper_chars = chars.upper()
    wrong="@# "

    if len(p) <= 8:
        return False
    
    lower, upper = 0, 0
    for ch in p:
        if ch in chars:
            lower += 1
        if ch in upper_chars:
            upper += 1
    if lower < 1 or upper < 1:
        return False
    
    i = 0
    while len(p) > i and p[i] not in wrong:
        i += 1
        return i == len(p)
    
    count = 0
    for n in p:
        if n.isdigit():
            count += 1
    if count <= 2: return False

    return True

# Lista a helyes jelszavak tárolására
good_passwords = []

while True:
    pwd = input("Adj meg egy jelszót: ")
    if is_correct_pwd(pwd):
        good_passwords.append(pwd)
    else:
        break

# Helyes jelszavak kiírása vesszővel elválasztva
print(", ".join(good_passwords))