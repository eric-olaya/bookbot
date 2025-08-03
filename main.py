from stats import count_words
from stats import count_characters
from stats import sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    # print(f"{count_words(contents)} words found in the document")
    # print(count_characters(contents))
    character_count = count_characters(contents)
    list = sort(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for item in list:
        key = item["char"]
        value = item["num"]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


main()