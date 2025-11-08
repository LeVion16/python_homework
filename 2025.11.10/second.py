def get_persons_stats() -> list[dict[str, int]]:
    print("Adjon meg neveket és a hozzájuk tartozó életkorokat! Kilépés ENTER-rel!")

    persons = []

    name = input("Neve: ")

    while name != "":

        age = int(input("Életkora: "))

        stats = {
            "Neve": name,
            "Kora": age
        }

        persons.append(stats)

        name = input("Neve: ")

    for stats in persons:
        print(f"Neve: {stats['Neve']} - Életkora: {stats['Kora']}")

get_persons_stats()