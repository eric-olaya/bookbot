def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(f"{count_words(contents)} words found in the document")

main()