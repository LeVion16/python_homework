def char_num(t: str) -> int:
    count = 0
    for ch in t:
        if ch.lower() == "a": 
            count += 1

    print(count)

char_num('alamfa')
char_num('AlmaFA')
char_num('Nemeth')


'''2. Feladat'''
def get_longest_num(nmbs: list) -> int:
    biggest = 0
    for n in nmbs:
        if n > biggest:
            biggest = n

    print(biggest)

numbers = [12, 43, 1, 100, 30]
get_longest_num(numbers)