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

def sort(dict):
    list_of_dicts = []
    for key in dict:
        current_dict = {}
        current_dict["char"] = key
        current_dict["num"] = dict[key]
        list_of_dicts.append(current_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(items):
    return items["num"]