from stats import split_words, times_char_appears, sort_report
import sys
def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
        return (file_contents)
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {split_words(book_text)} total words")
    print("---------- Character Count -------")
    print(sort_report(times_char_appears(book_text)))
    print("============= END ===============")
main()
