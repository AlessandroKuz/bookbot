import sys

from stats import get_words_number, get_char_number, get_sorted_items_dict


def get_book_text(filepath:str) -> str:
    with open(filepath, 'r') as f:
        file_contents: str = f.read()
    return file_contents

def print_report(book_path:str, num_words:int, sorted_char_dict:dict[str, int]):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for character, value in sorted_char_dict.items():
        if character.isalpha():
            print(f'{character}: {value}')

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path: str = sys.argv[1]
    contents: str = get_book_text(book_path)
    num_words: int = get_words_number(contents)
    char_dict: dict[str, int] = get_char_number(contents)
    sorted_char_dict: dict[str, int] = get_sorted_items_dict(char_dict)
    
    print_report(book_path, num_words, sorted_char_dict)

if __name__ == '__main__':
    main()

