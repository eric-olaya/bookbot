from stats import count_words
from stats import count_characters
from stats import sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    contents = get_book_text("./books/frankenstein.txt")
    # print(f"{count_words(contents)} words found in the document")
    # print(count_characters(contents))
    character_count = count_characters(contents)
    list = sort(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for item in list:
        key = item["char"]
        if key.isalpha():
            print(f"{key}: {item["num"]}")
    print("============= END ===============")


main()