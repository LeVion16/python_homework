def is_contain___a(w: str) -> int:
    '''Megvizsgálja h egy adott szóban hányszor szerepel az -a betű'''
    count = 0
    for ch in w:
        ch = ch.lower()
        if ch == 'a':
            count += 1
    return count

word = input("Adj meg egy szót: ")
print(is_contain___a(word))