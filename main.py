def get_book_text(filepath:str) -> str:
    with open(filepath, 'r') as f:
        file_contents: str = f.read()
    return file_contents

def main():
    contents: str = get_book_text('./books/frankenstein.txt')
    print(contents)

if __name__ == '__main__':
    main()

