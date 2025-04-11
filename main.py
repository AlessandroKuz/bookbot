from stats import get_words_number, get_char_number, get_sorted_items_dict


def get_book_text(filepath:str) -> str:
    with open(filepath, 'r') as f:
        file_contents: str = f.read()
    return file_contents

def main():
    contents: str = get_book_text('./books/frankenstein.txt')
    num_words: int = get_words_number(contents)
    char_dict: dict[str, int] = get_char_number(contents)
    sorted_char_dict: dict[str, int] = get_sorted_items_dict(char_dict)
    
    for character, value in sorted_char_dict.items():
        if character.isalpha():
            print(f'{character}: {value}')

if __name__ == '__main__':
    main()

