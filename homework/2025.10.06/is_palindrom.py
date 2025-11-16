def is_palindrom(w: str) -> bool:
    '''megnézi, hogy a szó visszafele is ugyanaz-e'''
    w = w.lower() # Mindent kisbetűvé alakítunk
    return w == w[::-1]

word = input("Adj meg egy szót, megnézem visszafele is ugyanaz-e: ")
print(is_palindrom(word))