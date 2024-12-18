def main():
    book_path ="books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_words = get_book_words(book_content)

    print(f"{book_words} words found in the document.")

def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_book_words(file_content):
    words = file_content.split()
    return len(words)

main()
