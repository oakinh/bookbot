def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_wordcount(text)
    # return(f"{wordcount} words found in the document")
    print(character_count(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_wordcount(text):
    words = text.split()
    return len(words)


def character_count(text):
    characters_in_text = {}
    lowered_text = text.lower()
    lowered_letters = []
    for letter in lowered_text:
        lowered_letters.append(letter)
    for letter in lowered_letters:
        if letter in characters_in_text:
            characters_in_text[letter] += 1
        else:
            characters_in_text[letter] = 1
    return characters_in_text

main()
