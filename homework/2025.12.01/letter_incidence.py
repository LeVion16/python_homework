def create_char_stats(text: str) -> dict[int]:
    stat = {}

    for i in text:
        if i not in stat.keys():
            stat[i] = 1
        else:
            stat[i] += 1

    print(stat)

text = input("Adj meg egy szöveget: ")
create_char_stats(text)