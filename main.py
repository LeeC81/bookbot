from stats import word_count
from stats import char_count



def get_book_text(file):
    with open(file) as f:
        file_txt = f.read()
        return file_txt



def main():
    text = get_book_text("./books/frankenstein.txt")
    num_of_chars = char_count(text)
    num_of_words = word_count(text)
    print (f"{num_of_words} words found in the document")
    print (num_of_chars)

main()
