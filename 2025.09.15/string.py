def sum_of_digits(num: int) -> int:
    '''Ez a függvény vissza adja a számjegyek összegét'''
    num = abs(num)  # előjel elhagyása
    summa = 0       # kezdőérték
    while num:      # addig, amíg van számjegy
        summa += num % 10   # az utólsó számjegyet hozzáadjuk
        num //= 10          # az utólsó számjegyet levágjuk
    return summa

def longest_word(words: list[str]) -> tuple[str, int]:
    '''Kiválasztja a leghoszabb szót, és kiírja mennyi karakterből áll'''
    max_word = words[0]               # induljunk az első szóval
    for w in words:                   # menjünk végig az összes szón
        if len(w) > len(max_word):    # ha hosszabb, mint a jelenlegi max
            max_word = w
    return max_word, len(max_word)    # visszaadjuk a szót és a hosszát

def is_contain(word: str) -> tuple[str, int]:
    '''Megszámolja, hogy mennyi a- betű van a szóban'''
    count = 0
    for ch in word:
        if ch.lower() == "a" in word:   # az aktuális betű kisbetűsítve "a"-e?
            count += 1
    return word, count

""" def is_valid_password(valid_password: str):
    '''Megvizsgálja a megadott jelszót, hogy megfelel-e a követelményeknek'''

        def contains_digit(w: str) -> bool:
            '''Megnézi, hogy tartalmaz-e számot a jelszó'''
            has_digit = False
            for ch in word:
                if ch.isdigit():
                    has_digit = True
            return has_digit
            
        def contains_upper(w: str) -> bool:
            '''Megnézi, hogy tartalmaz-e nagybetűt és kibetűt a jelszó'''
            has_upper = False
            for ch in word:
                if ch.isupper():
                    has_upper = True
            return has_upper
            
        given_password = ""
        while given_password != valid_password:
            if len(given_password) >= 8 and contains_digit(given_password) and contains_upper:
                given_password == valid_password
            return given_password """

input_num = int(input("Adj meg egy számot: "))
print(sum_of_digits(input_num))

print() # üres sor

words_list = ["gép", "rohangál", "kelepel", "ragad"]
print(longest_word(words_list))

print() # üres sor

word = input("Adj meg egy szót, megnézem mennyi 'a'- betű ban benne: ")
print(is_contain(word))

print() # üres sor

""" password = input("Adj meg egy jelszót: ")
print(is_valid_password(password)) """