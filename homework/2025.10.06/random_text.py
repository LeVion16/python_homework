import random as rr

def create_rondom_text(list: tuple[str]) -> str:
    '''Random számú betűsorozatot generál'''
    text = ""
    n = rr.randint(0, 44)
    for i in range(n):
        letter = rr.choice(list)
        text += letter
    return text

letters = ("a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű", "b", "c", "cs", "d", "dz", "dzs", "f", "g", "gy", "h","j", "k", "l", "ly","m", "n", "ny", "p", "q", "r", "s", "sz", "t", "ty", "v", "w", "x", "y", "z", "zs")
print(create_rondom_text(letters))