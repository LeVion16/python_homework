def reversed_print(w: str) -> str:
    """Vissszafele írja ki a szót"""
    return w[::-1]

word = input("Adj mege egy szót: ")
print(reversed_print(word))