def count_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    new_dict = {}
    for c in text:
    