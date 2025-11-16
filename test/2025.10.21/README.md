# A - feladat
Készíts egy függvényt (is_valid_pin), amely a paraméterül kapott string típusú pin-kód esetén logikai értékkel tér vissza attól függően, hogy a pin-kód érvényes-e!

    A kód érvénytelen, ha:
        • nem pont 4 karakter hosszú,
        • nullával kezdődik,
        • nem csak számot tartalmaz
        • egymás mellett azonos számok vannak.

    Példa a kimenetre:
        print(is_valid_pin("0123")) # False
        print(is_valid_pin("56123")) # False
        print(is_valid_pin("1223")) # False
        print(is_valid_pin("4133")) # False
        print(is_valid_pin("01a3")) # False
        print(is_valid_pin("4123")) # True


# B - feladat
Készíts egy digit_diff nevű függvényt, amely paraméterül kap egy számot. A függvény visszaadja a szám legnagyobb és legkisebb számjegye közötti különbséget. Amennyiben a szám kétszámjegynél kevesebb számjegyet tartalmaz, vagy mínusz szám, úgy -1-et adjon vissza!

    Példa a kimenetre:
        print(digit_diff(2856)) # 6
        print(digit_diff(-123)) # -1
        print(digit_diff(2)) # -1

Próbáld meg elkészíteni a feladatot úgy, hogy „q” leütéséig kéred be a számokat.