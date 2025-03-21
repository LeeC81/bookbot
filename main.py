from stats import word_count
from stats import char_count
from stats import sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        file_txt = f.read()
        return file_txt



def main():
    try:
        text = get_book_text(sys.argv[1])
        num_of_chars = char_count(text)
        num_of_words = word_count(text)
        sorted = sort_dict(num_of_chars)
        print (f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_of_words} total words
--------- Character Count -------''')
        for s in sorted:
            print (f"{s["char"]}: {s["count"]}")

        print ("============= END ===============")
    except Exception:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
