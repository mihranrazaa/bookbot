import sys

from stats import counter, final


def main():
    words = counter()
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
        """)
    final()
    print("============= END ===============")


main()
