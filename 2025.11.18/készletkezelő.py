stock = {"alma": 10, "banán": 5, "narancs": 0}

product = input("Termék: ")
if product.lower() in stock.keys():
    quantity = int(input("Mennyiség: "))
    if stock[product] - quantity >= 0:
        print(f"A vásárlás sikeres! Maradék: {stock[product] - quantity}")
    else:
        print("A vásárlás sikertelen! Nincsen ekkora mennyiség!")
else: print("Sikertelen vásárlás! Nincsen ilyen termék.")