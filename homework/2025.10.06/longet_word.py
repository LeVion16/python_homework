def longet_word(list: list[str]) -> tuple[str, int]:
    '''Kiválasztja a leghoszabb szót és annak hossát'''
    longest = ""
    for w in list:
        if len(w) > len(longest):
            longest = w
    return longest, len(longest)


words = ["alma", "körte", "szilva", "meggyleves", "banán"]
print(longet_word(words))