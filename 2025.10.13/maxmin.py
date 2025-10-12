import math

# A függvény adja vissza az input-paraméterként kapott számsorozat legnagyobb elemét!
def get_max(nums: list[int]) -> int:
    maxNum = nums[0]
    for i in range(1, len(nums), 1):
        if nums[i] > maxNum:
            maxNum = nums[i]
    return maxNum

# A függvény adja vissza az input-paraméterként kapott számsorozat legkisebb elemét!
def get_min(nums: list[int]) -> int:
    minNum = nums[0]
    for i in range(1, len(nums), 1):
        if nums[i] < minNum:
            minNum = nums[i]
    return minNum

# A függvény adja vissza az input-paraméterként kapott számsorozat legkisebb elemének a sorszámát!
def min_serial_number(nums: list[int]) -> int:
    index = 0
    min_num = nums[0]
    for i in range(1, len(nums), 1):
        if min_num > nums[i]:
            index, min_num = i, nums[i]
    return index + 1

# A függvény adja vissza az input-paraméterként kapott számsorozat legnagyobb elemének a sorszámát!
def max_serial_number(nums: list[int]) -> int:
    index = 0
    max_num = nums[0]
    for i in range(1, len(nums), 1):
        if nums[i] > max_num:
            index, max_num = i, nums[i]
    return index + 1

# A függvény visszaadja a megadott szóban a keresett karakter első előfordulásának a sorszámát.
# Ha nincs benne, -1-et ad vissza.
def serialnumber_of_char(word: str, c: str) -> int:
    i = 0
    while i < len(word) and word[i] != c:
        i += 1
    if i == len(word):  # ha végigment és nem találta
        return -1
    return i + 1  # sorszám 1-től számolva

# Tesztelés
numbers = [50, 100, 30, 47, 89, 2, 12]

print(get_max(numbers))
print(get_min(numbers))

print(f"A legkisebb elem indexe: {min_serial_number(numbers)}.")
print(f"A legnagyobb elem indexe: {max_serial_number(numbers)}.")

print(serialnumber_of_char("kalap", "a"))   # 2
print(serialnumber_of_char("kalap", "z"))   # -1

# A math-modul néhány "ajándéka":
"""
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(math.pi)
print(math.ceil(3.4))
print(math.floor(100.999))
print(math.pow(2, 10))
print(round(4.3))
print(round(4.9))
print(round(2.5))
print(round(3.5))
"""