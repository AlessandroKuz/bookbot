def get_words_number(text:str) -> int:
    words: list[str] = text.split()

    return len(words)

def get_char_number(text:str) -> dict[str, int]:
    text = text.lower()
    char_counts: dict[str, int] = {}
    for char in text:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    return char_counts

def get_sorted_items_dict(items_dict:dict[str, int]) -> dict[str, int]:
    sorted_chars: list[dict[str, str | int]] = [
        {'name': char, 'num': num} for char, num in items_dict.items()
    ]
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    sorted_char_dict: dict[str, int] = {dictionary['name']: dictionary['num'] for dictionary in sorted_chars}

    return sorted_char_dict

