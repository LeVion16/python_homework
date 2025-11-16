import math as m

'''1. feladat'''
def sum_of_digits(n: int) -> int:

    if n < 0:
        return 0

    numbers = []
    n = str(n)
    for ch in n:
        numbers.append(int(ch))

    total = sum(numbers)
    print(total)


sum_of_digits(123)
sum_of_digits(-123)


'''2. feladat'''
def get_longest_word(words: list) -> str:
    longest = ""
    for ch in words:
        if len(ch) > len(longest):
            longest = ch

    print(longest)


word_list = ["kalap", "csemege", "szelemen", "suhan", "végvár"]
get_longest_word(word_list)