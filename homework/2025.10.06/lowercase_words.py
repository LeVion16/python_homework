def lowercase_words(list: list[str]) -> None:
    '''mindent kisbetűssé alakít'''
    words = []
    for w in list:
        w = w.lower()
        words.append(w)
    return words

words = ["Alma", "Körte", "Szilva", "Banán"]
print(", ".join(lowercase_words(words)))