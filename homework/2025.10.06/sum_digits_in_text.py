def amount_digits(text: str) -> int:
    '''Megkeresi a szövegben az összes számjegyet és ezek összegét adja vissza.'''
    amount = 0
    for ch in text:
        if ch.isdigit():          # ha számjegy
            amount += int(ch)     # alakítsd számmá és add hozzá
    return amount

text = "Ma 2 alma és 3 körte van"
print(amount_digits(text))  # 👉 5
