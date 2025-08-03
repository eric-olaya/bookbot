from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(f"{count_words(contents)} words found in the document")
    print(count_characters(contents))

main()