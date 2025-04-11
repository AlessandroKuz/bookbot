def get_words_number(text:str) -> int:
    words: list[str] = text.split()

    return len(words)

