from stats import get_words_number, get_char_number


def get_book_text(filepath:str) -> str:
    with open(filepath, 'r') as f:
        file_contents: str = f.read()
    return file_contents

def main():
    contents: str = get_book_text('./books/frankenstein.txt')
    num_words: int = get_words_number(contents)
    char_dict: dict[str, int] = get_char_number(contents)
    print(char_dict)

if __name__ == '__main__':
    main()

