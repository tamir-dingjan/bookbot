def count_words(text):
    return len(text.split())


def count_unique_characters(text):
    force_lowercase = text.lower()
    unique_chars = {}
    for char in force_lowercase:
        if char in unique_chars.keys():
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars


with open("./books/frankenstein.txt") as f:
    text = f.read()
    print(count_words(text))
    print(count_unique_characters(text))
