def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    format_dictionary(characters_in_text, text)
    sort_list(list_of_dicts)
    # print(f"{wordcount} words found in the document")
    print(f"--- Begin report of {book_path} --- \n {wordcount} words found in the document")
    for item in list_of_dicts:
        print(f"The '{item['key']}' character was found {item['value']} times")

def sort_on(dict):
    return dict["value"]

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_wordcount(text):
    words = text.split()
    return len(words)

characters_in_text = {}
def character_count(text):
    
    lowered_text = text.lower()
    lowered_letters = []
    for text in lowered_text:
        lowered_letters.append(text)
    for letter in lowered_letters:
        if letter in characters_in_text:
            characters_in_text[letter] += 1
        else:
            characters_in_text[letter] = 1
    return characters_in_text

list_of_dicts = []
def format_dictionary(characters_in_text, text):
    character_count(text)
    for key, value in characters_in_text.items():
        if key.isalpha():
            new_dict = {"key": key, "value": value}
            list_of_dicts.append(new_dict)
    return(list_of_dicts)

def sort_list(list_of_dicts):
    return list_of_dicts.sort(reverse=True, key=sort_on)


# format_dictionary(characters_in_text)

main()
