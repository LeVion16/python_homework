def get_letter_stat(text: str) -> dict[str, int]:

    vowels = ("a", "e", "i", "o", "u")

    result = {
        'vowel': 0,
        'consonant': 0
    }

    for ch in text.lower():
        if ch in vowels: result["vowel"] += 1
        else: result["consonant"] += 1

    print(f"Az eredmény: ({text}) => {result}")

get_letter_stat("KUTYA")