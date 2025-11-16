def digit_diff(n: int) -> int:

    if n < 0: return -1 

    if len(str(n)) < 2: return -1 

    n = str(n)
    """ 
    Ez egy generátor kifejezés (int(ch) for ch in n), amit a max() függvény feldolgoz.
    Mit csinál pontosan:
        A for ch in n végigmegy az n karakterein: '2', '8', '5', '6'
        Az int(ch) minden karaktert számmá alakít: 2, 8, 5, 6
        A max() megkeresi ezek közül a legnagyobbat → 8
        Ez az érték kerül a max_n változóba.
    👉 Tehát a max_n itt 8 lesz. 
    """
    max_n = max(int(ch) for ch in n)
    min_n = min(int(ch) for ch in n)

    return max_n - min_n

"""     for i in n:
            if int(i) > max_n:
                max_n = int(i)
    
        for i in n:
            if int(i) < min_n:
                min_n = int(i) """

print(digit_diff(2856)) # 6
print(digit_diff(-123)) # -1
print(digit_diff(2)) # -1

inputValue = ""
while  inputValue.lower() != "q":
    inputValue = input("Adjon meg egy számot:  ")
    if inputValue.lower() != "q":
        print(digit_diff(int(inputValue)))