def count_words(text):
    return len(text.split())


def is_lowercase_letter(char):
    return "a" <= char <= "z"


def count_unique_characters(text):
    force_lowercase = text.lower()
    unique_chars = {}
    for char in force_lowercase:
        if char in unique_chars.keys():
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars


file = "books/frankenstein.txt"
with open(file) as f:
    text = f.read()

    print(f"--- Begin report of {file} ---")
    print(f"There are {count_words(text)} words in the document")

    for k, v in sorted(
        count_unique_characters(text).items(), key=lambda item: item[1], reverse=True
    ):
        if is_lowercase_letter(k):
            print(f"The {k} character was found {v} times")
    print("--- End of report ---")
