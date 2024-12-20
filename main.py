def main():
    book_path ="books/frankenstein.txt"
    book_content = get_book_content(book_path)
    book_words = get_book_words(book_content)
    chars_dict = get_chars_dic(book_content)
    
    print_report(book_path, book_words, chars_dict)

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

def sort_word_count_text(dict):
    return dict["count"]    


def print_report(book_path, words_count, chars_dict): 
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document.\n")

    word_count_text = []
    for c in chars_dict:
        if (c.isalpha()):
            word_count_text.append({'count': chars_dict[c], 'text': f"The '{c}' character was found {chars_dict[c]} times"})

    word_count_text.sort(reverse=True, key=sort_word_count_text)
    for dic in word_count_text:
        print(dic['text'])

    print("--- End report ---")
main()
