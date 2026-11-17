def count_words(text: str)-> int:
    words = text.split() # turns to list of words
    return len(words)

def count_characters(text: str)-> dict[str, int]:
    textski: str = text.lower()
    alphabetski: dict[str, int] = {}


    for char in textski:
        if char not in alphabetski:
            alphabetski[char] = 1
        else:
            alphabetski[char] += 1

    return alphabetski

def sort_on(unsorted: tuple[str, int]) -> int:
    return unsorted[1]

def chars_dict_to_sorted_list(unsorted_dict: dict[str, int])-> list[tuple[str, int]]:
    sorted_list: list[tuple[str, int]] = []

    for key in unsorted_dict:
        character = key
        count = unsorted_dict[key]
        sorted_list.append((character, count))

    sorted_list = sorted(sorted_list, reverse=True, key=sort_on)

    return sorted_list
