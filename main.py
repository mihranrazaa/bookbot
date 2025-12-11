def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return str(file_contents)


def counter():
    words = get_book_text().split()
    word_count = len(words)
    return word_count


def main():
    numbers = counter()
    print(f"Found {numbers} total words")


main()
