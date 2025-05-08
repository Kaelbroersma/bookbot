from stats import get_word_count, get_char_count, neat_char_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    wordcount = get_word_count(contents)
    char_count = get_char_count(contents)
    neatdict = neat_char_dict(char_count)
    print_report(path, wordcount, neatdict)
    return contents

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(path, wordcount, neatdict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for i in neatdict:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()
