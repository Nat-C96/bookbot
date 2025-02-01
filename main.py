def main():
    book_path = "/home/natvixen96/workplace/github.com/Nat-C96/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_characters(text)
    alphabet = pretty_report(letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for letter, count in alphabet:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")


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

def pretty_report(letters):
    alphabet_letter = []
    for i in letters:
        if i.isalpha() == True:
            alphabet_letter.append((i, letters[i]))
    alphabet_letter.sort(reverse=True, key=lambda x: x[1])
    return alphabet_letter






main()