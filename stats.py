def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return str(file_contents)


def counter():
    words = get_book_text().split()
    word_count = len(words)
    return word_count


def character_counter():
    character_dict = {}
    characters = get_book_text().lower()
    for char in characters:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict


print(character_counter())
