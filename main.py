import sys
from stats import (
    get_letter_count, 
    get_word_count, 
    get_sorted_list
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    num_words = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_list = get_sorted_list(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()