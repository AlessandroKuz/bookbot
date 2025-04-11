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

