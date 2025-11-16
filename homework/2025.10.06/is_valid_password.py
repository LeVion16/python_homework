def is_valid_password(w: str) -> str:
    '''Megnézi, hogy a megadott jelszó megfelel-e a követelményeknek'''
    value_1 = False
    value_2 = False
    value_3 = False

    if len(w) >= 8:
        value_1 = True
    for ch in w:
        if ch.isupper():
            value_2 = True
        if ch.isdigit():
            value_3 = True

    return "valid password!" if value_1 and value_2 and value_3 else "invalid password"

password = input("Add meg a jelszót: ")
print(is_valid_password(password))