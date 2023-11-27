from collections import Counter

FILENAME = "books/frankenstein.txt"
with open (FILENAME) as file:
    file_content = file.read()
    word_count = len(file_content.split())

    count_dict = Counter(letter.lower() for letter in file_content)
    sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    print(f"--- Begin report of {FILENAME} ---")
    print(f"{word_count} words found in the document\n")

    for entry, count in sorted_count_dict.items():
        if entry.isalpha():
            print(f"The '{entry}' character was found {count} times")
