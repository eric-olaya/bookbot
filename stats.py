def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_characters(text):
    dict = {}

    for char in text:
        lowercase = char.lower()
        if lowercase in dict:
            dict[lowercase] += 1
        else:
            dict[lowercase] = 1
    return dict