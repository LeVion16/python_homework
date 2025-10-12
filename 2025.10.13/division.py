def is_divisible(nums: tuple[int]) -> bool:
    value = ""
    for n in nums:
        if n % 3 == 0 and n % 4 == 0 and n % 6 == 0:
            value = True
    return value

def count_numbers(nums: tuple[int]) -> int:
    count = 0
    for n in nums:
        if n % 3 == 0 and n % 4 == 0 and n % 6 == 0:
            count += 1
    return count

def get_summa(nums: tuple[int]) -> int:
    valid_nums = []
    total = 0
    for n in nums:
        if n % 3 == 0 and n % 4 == 0 and n % 6 == 0:
            valid_nums.append(n)
    for i in valid_nums:
            total += i
    return total

def serial_number(nums: tuple[int]) -> int:
    i = 0   # számláló változó, kezdetben 0
    while i < len(nums):    # amíg i kisebb a nums hosszánál, megy a ciklus
        if nums[i] % 3 == 0 and nums[i] % 4 == 0 and nums[i] % 6 == 0:   # ha nums[i] osztható 3-mal, 4-gyel és 6-tal
            i += 1  # növeli i értékét eggyel
            return i    # visszatér i-vel (és kilép a függvényből)
    return -1   # ha semelyik szám nem jó, akkor -1-et ad vissza

def list_of_numbers(nums: tuple[int])  -> list:
    numbers = []
    for n in nums:
        if n % 3 == 0 and n % 4 == 0 and n % 6 == 0:
            numbers.append(n)
    return numbers

nums = (12, 24, 6, 30, 40)
print(is_divisible(nums))
print(count_numbers(nums))
print(get_summa(nums))
print(serial_number(nums))
print(list_of_numbers(nums))