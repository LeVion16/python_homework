def is_valid_pin(p: str) -> bool:

    # Ha nem pont 4 karakter
    count = 0
    for ch in p:
        count += 1
    if count != 4:
        return False
    
    # Ha 0-val kezdődik
    if p[0] == "0":
        return False
    
    # Ha nem csak számot tartalmaz
    if p != p.isdigit():
        return False
    
    # Ha egymás mellett azonos számok vannak
    for i in range(1, len(p), 1):
        if p[i] == p[i-1]:
            return False
    
    return True


print(is_valid_pin("0123")) # False
print(is_valid_pin("56123")) # False
print(is_valid_pin("1223")) # False
print(is_valid_pin("4133")) # False
print(is_valid_pin("01a3")) # False
print(is_valid_pin("4123")) # True