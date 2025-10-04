def count_letter_by_type(w: str, vowels: tuple, consonants: tuple) -> int:
    '''Magánhangzókat és mássalhangzókat számol'''
    total_1 = 0
    total_2 = 0
    w = w.lower()
    for ch in w:
        if ch in vowels:
            total_1 += 1
        elif ch in consonants:
            total_2 += 1
    return total_1, total_2

# Magyar ábécé magánhangzói
maganhangzok = ("a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű")

# Magyar ábécé mássalhangzói
massalhangzok = ("b", "c", "cs", "d", "dz", "dzs", "f", "g", "gy", "h","j", "k", "l", "ly","m", "n", "ny", "p", "q", "r", "s", "sz", "t", "ty", "v", "w", "x", "y", "z", "zs")

word = input("Adj meg egy szót: ")
print(count_letter_by_type(word, maganhangzok, massalhangzok))