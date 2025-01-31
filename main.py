def main():
    book_path = "/home/natvixen96/workplace/github.com/Nat-C96/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_characters(text)
    print(f"{num_words} words found in the document")
    print(letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    letters = {}
    lower_string = text.lower()
    for letter in lower_string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


main()