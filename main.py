from stats import count_words, count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str)-> str:
    with open(file_path) as f: #with deletes the opened file or wtv takes care of it after exits
        file_contents = f.read()
        return file_contents


def print_report(file_path: str, word_count: int, character_list: list[tuple[str, int]])-> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in character_list:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) <=1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]


    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text) #dict of character counts
    sorted_character_count_list = chars_dict_to_sorted_list(character_count)
    # print(f"Found {word_count} total words")
    # print(sorted_character_count_list)
    print_report(book_path, word_count, sorted_character_count_list)


main()
