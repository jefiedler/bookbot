def main():
    book_path ="books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_words = get_book_words(book_content)
    chars_dict = get_chars_dic(book_content)
    

def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_book_words(file_content):
    words = file_content.split()
    return len(words)

def get_chars_dic(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
