import sys


def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
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


def sort_on(items):
    print(items["num"])


def final():
    character_dict = character_counter()
    sorted_dict = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    for char, num in sorted_dict:
        if char.isalpha():
            print(f"{char}: {num}")


final()
