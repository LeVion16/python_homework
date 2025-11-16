def sum_of_digits(num: int) -> int:
    '''Összeadja a megadott szám számjegyeit'''
    total = 0
    for i in str(num):
        total += int(i)
    return total

value = int(input("Adj meg egy számot és összeadom a számjegyeit: "))
print(sum_of_digits(value))